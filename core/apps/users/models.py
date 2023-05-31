from django.db import models
# Create your models here.

class Users(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Email: {self.email} - Name: {self.name}"
    