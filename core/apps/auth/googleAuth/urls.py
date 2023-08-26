from django.urls import path
from .views import GoogleLogin, GoogleRegister

urlpatterns = [
    path("register", GoogleRegister.as_view()),
    path("login", GoogleLogin.as_view()),
]
