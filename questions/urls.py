from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', GetCategories),
    path('questions/', DrawQuestions),
]
