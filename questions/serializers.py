from rest_framework import serializers

from users.models import User

from .models import Hint, Question, Theme


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'theme_id')

    theme_id = serializers.IntegerField(write_only=True)


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'title', 'author', 'is_private', 'questions')

    author = serializers.CharField(write_only=True, required=False)
    is_private = serializers.CharField(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    def create(self, validated_data):
        request_user = self.context['request'].user
        try:
            user = User.objects.get(email=request_user)
            validated_data['author'] = user
            theme = Theme.objects.create(**validated_data)
            return theme
        except User.DoesNotExist:
            return None


class ThemeDetailSerializer(ThemeSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'title', 'is_private', 'questions')

    author = None
    questions = QuestionSerializer(many=True)


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('text', 'question')
