from rest_framework import serializers
from .models import *


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["id", "title", "description"]
