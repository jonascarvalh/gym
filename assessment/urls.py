from django.urls import path, include
from assessment.views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment_view, name='enrollment_view'),
]