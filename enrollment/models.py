from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    choice = (
        ('Ex', 'Público Externo'),
        ('E', 'Estudante'), 
        ('F', 'Funcionário')
    )
        
    name          = models.CharField(max_length=100, null=False)
    cpf           = models.CharField(max_length=11, unique=True, null=False)
    sig_register  = models.CharField(max_length=11, unique=True)
    ocupation     = models.CharField(max_length=2, choices=choice, null=False)
    is_registered = models.BooleanField()
    
    def __str__(self):
        return self.name