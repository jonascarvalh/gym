from django.urls import path, include
from enrollment.views import *

app_name = 'enrollment'

urlpatterns = [
    path('', enrollment_view, name='enrollment_view'),
]