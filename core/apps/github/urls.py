from django.urls import path
from .views import RegisterGithub

urlpatterns = [
    path("register", RegisterGithub.as_view()),
]
