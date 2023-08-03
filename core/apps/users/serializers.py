from rest_framework import serializers
from .models import NotemeUser


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotemeUser
        fields = ["email", "username", "first_name", "last_name", "password"]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotemeUser
        fields = ["email", "password"]
