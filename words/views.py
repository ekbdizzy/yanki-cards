from django.conf import settings
from django.db import transaction

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
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
def create_new_translation_view(request):  # noqa CCR001
    """Create new phrases and translations stack."""
    serializer = PhraseSerializer(data=request.data, many=True)
    serializer.is_valid()

    phrases = []
    for phrase_data in serializer.validated_data:
        phrase, created = Phrase.objects.get_or_create(**phrase_data)
        phrases.append(phrase)

    stack = TranslationsStack.objects.filter(
        phrases__in=phrases,
        user=request.user,
    ).first()
    if stack:
        for phrase in phrases:
            if phrase not in stack.phrases.all():
                stack.phrases.add(phrase)
    else:
        stack = TranslationsStack.objects.create(user=request.user)
        stack.phrases.add(*phrases)

    serializer = TranslationsStackSerializer(data=stack)
    serializer.is_valid(raise_exception=True)

    return Response(serializer, status=status.HTTP_201_CREATED)
