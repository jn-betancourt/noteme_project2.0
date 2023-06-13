from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
