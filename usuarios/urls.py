from django.urls import path, include
from usuarios.views import register_view, register_create, login_view, login_create

app_name = 'usuarios'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register_create/', register_create, name='register_create'),
    path('login/', login_view, name='login'),
    path('login_create/', login_create, name='login_create')
]