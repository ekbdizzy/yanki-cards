from rest_framework import serializers

from .models import Phrase, TranslationsStack


class PhraseSerializer(serializers.ModelSerializer):
    phrase = serializers.CharField(max_length=60)

    class Meta:
        model = Phrase
        fields = ('phrase', 'language')


class TranslationsStackSerializer(serializers.ModelSerializer):
    phrases = PhraseSerializer(many=True)

    class Meta:
        model = TranslationsStack
        fields = ('id', 'phrases', 'created_at')
