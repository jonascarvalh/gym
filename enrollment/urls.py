from django.urls import path, include
from enrollment.views import *

app_name = 'enrollment'

urlpatterns = [
    path('', enrollment_view, name='enrollment_view'),
    path('search/', search, name='search'),
    path('matricular/', register_view, name='register_view')
]