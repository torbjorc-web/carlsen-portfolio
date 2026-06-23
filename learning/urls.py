from django.urls import path
from . import views

urlpatterns = [
    path('', views.learning_list, name='learning_list'),
]
