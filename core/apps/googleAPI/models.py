from django.db import models
from ..users.models import NotemeUser

# Create your models here.


# The `GoogleUsers` class represents a model for storing information about users who have
# authenticated with Google.
class GoogleUsers(models.Model):
    class Meta:
        verbose_name = "google_user"
        verbose_name_plural = "google_users"

    google_id = models.CharField(
        max_length=255, null=False, unique=True, primary_key=True
    )
    token_id = models.CharField(max_length=255, null=False, unique=True)
    account = models.ForeignKey(NotemeUser, on_delete=models.CASCADE)
