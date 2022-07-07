from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Phrase, TranslationsStack


class PhraseSerializer(serializers.ModelSerializer):
    phrase = serializers.CharField(max_length=60, required=True)
    language_code = serializers.CharField(max_length=2, required=True)

    class Meta:
        model = Phrase
        fields = ('phrase', 'language_code')

    def validate_language_code(self, value):
        codes = settings.AVAILABLE_LANGUAGE_CODES
        if value not in codes:
            raise ValidationError(f'Language code should be on of {codes}.')
        return value


class TranslationsStackSerializer(serializers.ModelSerializer):
    phrases = PhraseSerializer(many=True)

    class Meta:
        model = TranslationsStack
        fields = ('id', 'phrases', 'created_at')
