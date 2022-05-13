from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WordSerializer
from .yandex_services import get_yandex_token, translate_word


def parse_language_code(word: str) -> str:
    """If contains cyrillic - return 'ru', else 'en'."""
    # TODO add parsing of cyrillic letters
    return 'en'


@api_view(['POST'])
@permission_classes([AllowAny])
def get_translation_view(request):
    """Translate word and return translation."""
    serializer = WordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    word = serializer.validated_data.get('word')
    token = get_yandex_token(settings.YA_OAUTH_TOKEN)
    translation = translate_word(
        token=token,
        word=word,
        language_code=parse_language_code(word),
    )
    return Response(translation)


class WordListCreateView(APIView):
    permission_classes = [IsAuthenticated]
