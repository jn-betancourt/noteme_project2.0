from django.urls import path
from .views import GoogleRegister, GoogleLogin

urlpatterns = [
    path("register", GoogleRegister.as_view()),
    path("login", GoogleLogin.as_view()),
]
