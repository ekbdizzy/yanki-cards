from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        ref_name = 'Yanki User'
        model = User
        fields = ("first_name", "last_name", "email", "password")
