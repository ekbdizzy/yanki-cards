from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)