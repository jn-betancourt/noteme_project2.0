from django.urls import path
from .views import UserCreation, UserAuth

urlpatterns = [
    path("signUp", UserCreation.as_view()),
    path("logIn", UserAuth.as_view())
]
