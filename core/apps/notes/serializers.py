from rest_framework import serializers
from .models import Note


# The `NoteSerializer` class is a serializer for the `Note` model with fields `note_id`, `title`, and
# `description`.
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["note_id", "title", "description"]
