from itertools import chain

from django.conf import settings
from django.db import transaction

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Phrase, TranslationsStack
from .serializers import PhraseSerializer, TranslationsStackSerializer
from .yandex_services import get_yandex_token, translate_phrase


def parse_language_code(word: str) -> str:
    """If contains cyrillic - return 'ru', else 'en'."""
    # TODO add parsing of cyrillic letters
    return 'en'


@api_view(['POST'])
@permission_classes([AllowAny])
def get_translation_view(request):
    """Translate word and return translation."""
    serializer = PhraseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phrase = serializer.validated_data.get('phrase')
    token = get_yandex_token(settings.YA_OAUTH_TOKEN)
    translation = translate_phrase(
        token=token,
        phrase=phrase,
        language_code=parse_language_code(phrase),
    )
    return Response(translation)


@api_view(['POST'])
@permission_classes([AllowAny])
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

        case _:  # there are more than one stack.
            phrases = set(
                chain.from_iterable([s.phrases.all() for s in stacks]),
            )
            stack = stacks.first()
            for phrase in phrases:
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
        return TranslationsStack.objects.filter(user=self.request.user)
