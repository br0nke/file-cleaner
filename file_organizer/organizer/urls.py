from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_organizer, name='file_organizer'),
]