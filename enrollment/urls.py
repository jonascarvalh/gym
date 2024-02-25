from django.urls import path, include
from enrollment.views import *

app_name = 'enrollment'

urlpatterns = [
    path('', enrollment_view, name='enrollment_view'),
    path('busca/', search, name='search'),
    path('matricular/', add_view, name='add_view'),
    path('criar_matricula/', add_create, name='add_create'),
    path('<int:id>/', to_view, name='to_view'),
    path('editar/<int:id>/', to_edit, name='to_edit'),
    path('editar_matricula/<int:id>', edit_create, name='edit_create'),
]