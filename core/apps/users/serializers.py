from rest_framework import serializers
from .models import *


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "email", "name", "password"]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "email", "password"]
