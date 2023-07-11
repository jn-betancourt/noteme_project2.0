from django.db import models


# Create your models here.
class GoogleAccount(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    picture = models.URLField(default=None)
    is_verified = models.BooleanField()
    account_provider = models.CharField(max_length=255)
