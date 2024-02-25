from django.db import models
from enrollment.models import Registration

# Create your models here.
class Assessment(models.Model):
    choice_is_evaluated = (
        ('True', 'Avaliado'),
        ('False', 'Não Avaliado')
    )

    name   = models.ForeignKey(Registration, on_delete=models.DO_NOTHING)
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False) 
    imc    = models.FloatField(null=False)
    is_evaluated = models.CharField(max_length=5, choices=choice_is_evaluated)

    def __str__(self):
        return f'{self.name}'