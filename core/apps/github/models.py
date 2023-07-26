from django.db import models
from ..users.models import Users

# Create your models here.


class GithubUsers(models.Model):
    class Meta:
        verbose_name = "github_user"
        verbose_name_plural = "github_users"

    account = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    github_code = models.CharField(max_length=255)
