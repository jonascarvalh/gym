from django.urls import path, include
from assessment.views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment_view, name='assessment_view'),
    path('buscar/', search, name='search'),
    path('avaliar/', add_view, name='add_view'),
    path('criar_avaliacao/', add_create, name='add_create'),
    path('<int:id>/', to_view, name='to_view'),
    path('<int:id>/editar', to_edit, name='to_edit'),
    path('<int:id>/editar_avaliacao', edit_create, name='edit_create'),
    path('<int:id>/delete', delete_create, name='delete_create'),
]