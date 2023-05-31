from django.db import models
from ..users.models import Users

# Create your models here.


class Notes(models.Model):
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user_id")

    def __str__(self):
        return f"{self.title}\n{self.description}"
