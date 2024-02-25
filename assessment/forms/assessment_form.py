from django import forms
from utils.django_forms import *
from assessment.models import Assessment
from enrollment.models import Registration
from django.shortcuts import get_object_or_404

class AssessmentForm(forms.ModelForm):
    choice_is_evaluated = (
        ('True', 'Avaliado'),
        ('False', 'Não Avaliado')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i, value in self.fields.items():
            add_attr(self.fields[i], 'class', 'form-control')

    class Meta:
        model = Assessment
        fields = [
            'name',
            'height',
            'weight',
            'imc',
            'is_evaluated'
        ]

    name = forms.ModelChoiceField(
        required=True,
        label='Nome:',
        widget=forms.Select(attrs={'disabled': False}),
        queryset=Registration.objects.all(),
        validators=[validate_user],
    )

    height = forms.CharField(
        error_messages={'required': 'Digite uma altura.'},
        required=True,
        label='Altura:',
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    weight = forms.CharField(
        required=True,
        label='Peso:',
        error_messages= {'required': 'Esse campo não pode ser vazio.'},
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    imc = forms.CharField(
        required=True,
        error_messages={'required': 'Este Campo é obrigatório.'},
        label='IMC:',
        help_text=(
            'Este campo é calculado de forma automática.'
        ),
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    is_evaluated = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'disabled': False}),
        error_messages={'required': 'Este campo é obrigatório.'},
        label='Status da Avaliação:',
        choices=choice_is_evaluated,
    )

    def clean_height(self):
        height = self.cleaned_data.get('height', '')
        height = height.replace(',', '.')
        try:
            height = float(height)
        except:
            raise forms.ValidationError(
                'A altura precisa ser um número inteiro ou decimal!',
                code='invalid',
            )
        
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get('weight', '')
        weight = weight.replace(',', '.')
        try:
            weight = float(weight)
        except:
            raise forms.ValidationError(
                'O peso precisa ser um número inteiro ou decimal!',
                code='invalid',
            )
        
        return weight


    def clean(self):
        cleaned_data = super().clean()