from django.urls import path
from .views import Person

urlpatterns = [
    path('',Person, name = 'person_list'),
]