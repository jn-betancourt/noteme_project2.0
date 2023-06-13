from django.urls import path
from .views import *

urlpatterns = [
    path("getNotes", NotesManagement.as_view()),
    path("modNote", NotesManagement.as_view()),
]
