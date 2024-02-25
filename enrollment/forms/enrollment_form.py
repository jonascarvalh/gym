from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import *
from enrollment.models import Registration

class RegisterForm(forms.ModelForm):
    choice_ocupation = [
        ('', 'Selecione'),
        ('E', 'Estudante'), 
        ('Ex', 'Público Externo'),
        ('F', 'Funcionário')
    ]

    choice_registered = [
        ('', 'Selecione'),
        ('True', 'Matriculado'),
        ('False', 'Não Matriculado'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name'], 'Nome Completo')
        add_placeholder(self.fields['cpf'], 'CPF')
        add_placeholder(self.fields['sig_register'], 'Matrícula no SIG')

        for i, value in self.fields.items():
            add_attr(self.fields[i], 'class', 'form-control')

    class Meta:
        model = Registration
        fields = [
            'name',
            'cpf',
            'sig_register',
            'ocupation',
            'is_registered'
        ]

    name = forms.CharField(
        error_messages={'required': 'Digite um nome.'},
        required=True,
        label='Nome:',
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    cpf = forms.CharField(
        error_messages={'required': 'Digite um CPF.'},
        required=True,
        label='CPF:',
        validators=[validate_cpf],
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    sig_register = forms.CharField(
        required=False,
        label='Matrícula do SIG:',
        help_text=(
            'Caso seja um Estudante ou Funcionário este campo é obrigatório.'
        ),
        error_messages= {'required': 'Esse campo não pode ser vazio.'},
        validators=[validate_sig],
        widget=forms.TextInput(attrs={'disabled': False}),
    )

    ocupation = forms.ChoiceField(
        required=True,
        error_messages={'required': 'Este Campo é obrigatório.'},
        label='Ocupação:',
        widget=forms.Select(attrs={'disabled': False}),
        choices=choice_ocupation,
    )

    is_registered = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'disabled': False}),
        error_messages={'required': 'Este campo é obrigatório.'},
        label='Matriculado',
        choices=choice_registered,
    )

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '')
        instance = self.instance
        if instance and instance.pk:
            exists = Registration.objects.exclude(pk=instance.pk).filter(cpf=cpf).exists()
        else:
            exists = Registration.objects.filter(cpf=cpf).exists()

        if exists:
            raise forms.ValidationError(
                'Este CPF já foi cadastrado!',
                code='invalid',
            )
        return cpf
    
    def clean_sig_register(self):
        sig_register = self.cleaned_data.get('sig_register', '')
        instance = self.instance
        if instance and instance.pk:
            exists = Registration.objects.exclude(pk=instance.pk).filter(sig_register=sig_register).exists()
        else:
            exists = Registration.objects.filter(sig_register=sig_register).exists()

        if exists:
            raise forms.ValidationError(
                'Essa matrícula já está no sistema!',
                code='invalid',
            )
        return sig_register
    
    def clean(self):
        cleaned_data = super().clean()