from rest_framework import serializers

from users.models import User

from .models import Hint, Question, Theme


class HintSerializer(serializers.ModelSerializer):

    question_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Hint
        fields = ('id', 'text', 'question_id')


class QuestionSerializer(serializers.ModelSerializer):

    theme_id = serializers.IntegerField(write_only=True)
    hints = HintSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'text', 'theme_id', 'hints')


class ThemeSerializer(serializers.ModelSerializer):

    author = serializers.CharField(write_only=True, required=False)
    is_private = serializers.CharField(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ('id', 'title', 'author', 'is_private', 'questions')

    def create(self, validated_data):
        request_user = self.context['request'].user
        user = User.objects.get(email=request_user)
        validated_data['author'] = user
        theme = Theme.objects.create(**validated_data)
        return theme


class ThemeDetailSerializer(ThemeSerializer):

    author = None
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Theme
        fields = ('id', 'title', 'is_private', 'questions')
