from django.urls import path, include
from assessment.views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment_view, name='assessment_view'),
    path('buscar/', search, name='search'),
    path('avaliar/', add_view, name='add_view'),
    path('criar_avaliacao/', add_create, name='add_create')
]