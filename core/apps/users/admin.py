from django.contrib import admin
from .models import NotemeUser

# Register your models here.


@admin.register(NotemeUser)
class NotemeUsersAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "date_joined", "provider"]
