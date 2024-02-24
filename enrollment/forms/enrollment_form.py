from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_attr, add_placeholder, strong_password
from enrollment.models import Registration

class RegisterForm(forms.ModelForm):
    choice_ocupation = [
        ('E', 'Estudante'), 
        ('Ex', 'Público Externo'),
        ('F', 'Funcionário')
    ]

    choice_registered = [
        ('True', 'Matriculado'),
        ('False', 'Não Matriculado'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name'], 'Nome Completo')
        add_placeholder(self.fields['cpf'], 'CPF')
        add_placeholder(self.fields['sig_register'], 'Matrícula no SIG')
        add_placeholder(self.fields['ocupation'], 'Selecione')
        # add_placeholder(self.fields['is_registered'], 'Selecione')

        for i, value in self.fields.items():
            add_attr(self.fields[i], 'class', 'form-control')
            # if self.fields[i].help_text == '':
            #     add_attr(self.fields[i], 'class', 'mb-3')

    class Meta:
        model = User
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
        label='Nome:'
    )

    cpf = forms.CharField(
        error_messages={'required': 'Digite um CPF.'},
        required=True,
        label='CPF:'
    )

    sig_register = forms.CharField(
        label='Matrícula do SIG:',
        help_text=(
            'Caso seja um Estudante ou Funcionário este campo é obrigatório.'
        ),
        error_messages= {'required': 'Esse campo não pode ser vazio.',},
    )

    ocupation = forms.ChoiceField(
        error_messages={'required': 'Este Campo é obrigatório.'},
        label='Ocupação:',
        widget=forms.Select(choices=choice_ocupation),
        choices=choice_ocupation
    )

    is_registered = forms.ChoiceField(
        required=True,
        widget=forms.Select(choices=choice_registered),
        error_messages={'required': 'Este campo é obrigatório.'},
        validators=[],
        label='Matriculado',
        choices=choice_registered
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'O e-mail já está sendo utilizado!',
                code='invalid',
            )
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise ValidationError(
                'Este nome de usuário já está sendo utilizado!',
                code='invalid',
            )
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password is None:
            return
        
        if password != password2:
            password_confirmation_error = ValidationError(
                'As senhas digitadas não são iguais.',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                # 'password2': [
                #     password_confirmation_error,
                # ],
            })