from django.urls import path, include
from enrollment.views import *

app_name = 'enrollment'

urlpatterns = [
    path('', enrollment_view, name='enrollment_view'),
    path('busca/', search, name='search'),
    path('matricular/', add_view, name='add_view'),
    path('criar_matricula/', add_create, name='add_create')
]