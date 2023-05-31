from django.urls import path
from .views import *

urlpatterns = [
    path("create", UserManagement.as_view()),
    path("getUser", UserManagement.as_view()),
]
