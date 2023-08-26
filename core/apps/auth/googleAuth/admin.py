from django.contrib import admin
from .models import GoogleUsers
# Register your models here.

@admin.register(GoogleUsers)
class GoogleAccountsAdmin(admin.ModelAdmin):
    list_display = ["account"]