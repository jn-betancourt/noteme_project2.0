from django.urls import path
from .views import *

urlpatterns = [
    path("getNotes", NotesManagement.as_view()),
    path("createNote", NotesManagement.as_view()),
    path("delNote", NotesManagement.as_view()),
    path("modNote", NotesManagement.as_view())
]