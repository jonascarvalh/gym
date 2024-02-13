from django.urls import path
from usuarios.views import register_view, register_create

app_name = 'usuarios'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register_create/', register_create, name='register_create'),
]