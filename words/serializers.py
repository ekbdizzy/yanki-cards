from rest_framework import serializers

from .models import Phrase, TranslationsStack


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('phrase', 'language')


class TranslationsStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationsStack
        fields = ('phrases', 'created_at')

    # phrases = PhraseSerializer(many=True)
