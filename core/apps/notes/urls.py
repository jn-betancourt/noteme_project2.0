from django.urls import path
from .views import *

# The `urlpatterns` variable is a list of URL patterns that map URLs to view functions or classes in a
# Django application. In this case, there are two URL patterns defined:
urlpatterns = [
    path("getNotes", NotesManagement.as_view()),
    path("modNote", NotesManagement.as_view()),
]
