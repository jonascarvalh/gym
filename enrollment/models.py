from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    choice = (
        ('Ex', 'Público Externo'),
        ('E', 'Estudante'), 
        ('F', 'Funcionário')
    )

    ocupation = models.CharField(max_length=2, choices=choice)
    cpf = models.CharField(max_length=11, unique=True)
    sig_register = models.CharField(max_length=11, unique=True)
    is_registered = models.BooleanField()

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'