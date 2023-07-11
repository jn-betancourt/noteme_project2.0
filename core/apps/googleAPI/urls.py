from django.urls import path
from .views import *

urlpatterns = [
    path("googleRegister", GoogleRegister.as_view()),
]
