from django.urls import path
from usuarios.views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
]