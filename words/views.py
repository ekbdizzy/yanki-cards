import codecs
import csv
from itertools import chain

from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.utils import dateformat, timezone

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Phrase, TranslationsStack
from .serializers import PhraseSerializer, TranslationsStackSerializer
from .yandex_services import get_yandex_token, translate_phrase


@api_view(['POST'])
@permission_classes([AllowAny])
def get_translation_view(request):
    """Translate word and return translation.
    :phrase: Phrase or word on any available language
    :language_code: destination language code: en | ru | tr."""
    serializer = PhraseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phrase = serializer.validated_data.get('phrase')
    language_code = serializer.validated_data.get('language_code')
    token = get_yandex_token(settings.YA_OAUTH_TOKEN)
    translation = translate_phrase(
        token=token,
        phrase=phrase,
        language_code=language_code,
    )
    return Response(translation)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def create_new_translation_view(request):
    """Create new phrases and translations_stack.
    Remove collisions if translations_stacks more than one.
    Return created or updated translation_stack in Response."""
    serializer = PhraseSerializer(data=request.data, many=True)
    serializer.is_valid()

    phrases = []
    for phrase_data in serializer.validated_data:
        phrase, _ = Phrase.objects.get_or_create(**phrase_data)
        phrases.append(phrase)

    stacks = (
        TranslationsStack.objects.filter(
            user=request.user,
            phrases__in=phrases,
        )
        .prefetch_related('phrases')
        .distinct()
    )

    match stacks.count():

        case 0:  # stack does not exists:
            stack = TranslationsStack.objects.create(user=request.user)
            stack.phrases.set(phrases)

        case 1:  # there is only one stack:
            stack = stacks.first()
            for phrase in phrases:
                if phrase not in stack.phrases.all():
                    stack.phrases.add(phrase)

        case _:  # there are more than one stack:
            phrases_set = set(
                chain.from_iterable([s.phrases.all() for s in stacks]),
            ).union(phrases)
            stack = stacks.first()
            for phrase in phrases_set:
                if phrase not in stack.phrases.all():
                    stack.phrases.add(phrase)
            stacks_ids = [stack.id for stack in stacks]
            stacks_ids.remove(stack.id)
            TranslationsStack.objects.filter(id__in=stacks_ids).delete()

    stack_serializer = TranslationsStackSerializer(stack)
    return Response(stack_serializer.data, status=status.HTTP_201_CREATED)


class TranslationsStackView(ListAPIView):
    """List of user's translations of words."""

    permission_classes = [IsAuthenticated]
    serializer_class = TranslationsStackSerializer

    def get_queryset(self):
        user = self.request.user
        return user.translations.all()


class TranslationsStackDeleteView(DestroyAPIView):
    """Delete translations stack."""

    permission_classes = [IsAuthenticated]
    serializer_class = TranslationsStackSerializer

    def get_queryset(self):
        return TranslationsStack.objects.filter(user=self.request.user.id)


def _get_csv_file_name(request):
    formatted_date = dateformat.format(timezone.now(), "d_m_Y")
    user_name, _ = request.user.email.split("@")
    return f"yanki_{user_name}_{formatted_date}.csv"


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_anki_cards_view(request):
    """Download csv file with anki cards on selected languages.
    Should have param "lang" with pair language codes(?lang=ru,en)."""

    languages = request.GET.get('lang')
    if languages is None:
        return Response(
            {"error": "Should have param 'lang' with languages: (?lang=ru,en)"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    lang1, lang2 = languages.split(',')
    translations_stacks = TranslationsStack.objects.filter(
        user=request.user,
    )
    pairs = []
    for stack in translations_stacks:
        phrases = stack.phrases.filter(
            Q(language_code=lang1) | Q(language_code=lang2),
        )
        phrases_pair = [phrase.phrase for phrase in phrases]
        if len(phrases_pair) == 2:
            pairs.append(phrases_pair)

    csv_file_name = _get_csv_file_name(request)
    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition': f'attachment; filename="{csv_file_name}"',
        },
    )
    response.write(codecs.BOM_UTF8)
    csv_writer = csv.writer(response, delimiter='\t')
    for pair in pairs:
        csv_writer.writerow(pair)
        csv_writer.writerow(reversed(pair))

    return response
