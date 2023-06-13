from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="user_id"
    )

    def __str__(self):
        return f"{self.title} : {self.description}"
