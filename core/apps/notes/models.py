from django.db import models
from ..users.models import NotemeUser

# Create your models here.


# The `Note` class represents a model for storing notes with a unique identifier, title, description,
# and a foreign key to the `Users` model.
class Note(models.Model):
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    note_id = models.CharField(primary_key=True, unique=True, max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    account = models.ForeignKey(NotemeUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} : {self.description}"
