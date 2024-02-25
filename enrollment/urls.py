from django.urls import path, include
from enrollment.views import *

app_name = 'enrollment'

urlpatterns = [
    path('', enrollment_view, name='enrollment_view'),
    path('busca/', search, name='search'),
    path('matricular/', add_view, name='add_view'),
    path('criar_matricula/', add_create, name='add_create'),
    path('<int:id>/', to_view, name='to_view'),
    path('<int:id>/editar', to_edit, name='to_edit'),
    path('<int:id>/editar_matricula', edit_create, name='edit_create'),
    path('<int:id>/delete', delete_create, name='delete_create'),
]