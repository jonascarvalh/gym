from django.urls import path, include
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home_view'),
]