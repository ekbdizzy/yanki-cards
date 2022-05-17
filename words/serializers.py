from rest_framework import serializers

from .models import Phrase, TranslationsStack


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('phrase', 'language')

    phrase = serializers.CharField(max_length=60)


class TranslationsStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationsStack
        fields = ('phrases', 'created_at')

    phrases = PhraseSerializer(many=True)
