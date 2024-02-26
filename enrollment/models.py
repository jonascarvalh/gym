from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    choice_ocupation = (
        ('Ex', 'Público Externo'),
        ('E', 'Estudante'), 
        ('F', 'Funcionário')
    )

    choice_is_registered = (
        ('True', 'Matriculado'),
        ('False', 'Não Matriculado')
    )
        
    name          = models.CharField(max_length=100, null=False)
    cpf           = models.CharField(max_length=11, unique=True, null=False)
    sig_register  = models.CharField(max_length=11)
    ocupation     = models.CharField(max_length=2, choices=choice_ocupation, null=False)
    is_registered = models.CharField(max_length=5, choices=choice_is_registered)
    
    def __str__(self):
        return self.name