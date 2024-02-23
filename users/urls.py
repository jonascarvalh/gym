from django.urls import path, include
from users.views import register_view, register_create, login_view, login_create, logout_view, menu_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register_create/', register_create, name='register_create'),
    path('login/', login_view, name='login'),
    path('login_create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('menu/', menu_view, name='menu')
]