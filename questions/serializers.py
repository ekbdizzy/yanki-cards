from rest_framework import serializers

from users.models import User

from .models import Hint, Question, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('title', 'author', 'is_private')

    author = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        request_user = self.context['request'].user
        try:
            user = User.objects.get(email=request_user)
            theme = Theme.objects.create(author=user, **validated_data)
            return theme
        except User.DoesNotExist:
            return None


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('text', 'question')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'author', 'theme')
