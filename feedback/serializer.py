from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):

    user = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Feedback
        fields = ("theme", "title", "text", "user")
