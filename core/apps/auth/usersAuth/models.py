from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db import models


class NotemeUser(AbstractUser):
    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"

    email = models.EmailField(primary_key=True, unique=True)
    provider = models.CharField(max_length=30)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    The above function creates an authentication token for a user when a new user is created.

    :param sender: The `sender` parameter refers to the model class that is sending the signal. In this
    case, it is `settings.AUTH_USER_MODEL`, which is the user model specified in the Django settings
    :param instance: The `instance` parameter refers to the instance of the model that triggered the
    signal. In this case, it refers to the instance of the `User` model that was just created
    :param created: The `created` parameter is a boolean value that indicates whether a new instance of
    the `sender` model has been created or an existing instance has been updated. It is set to `True` if
    a new instance is created, and `False` if an existing instance is updated, defaults to False
    (optional)
    """
    if created:
        Token.objects.create(user=instance)
