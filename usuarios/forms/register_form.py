from django import forms
from usuarios.models import Registration
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_attr, add_placeholder, strong_password

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['first_name'], 'Seu nome')
        add_placeholder(self.fields['last_name'], 'Seu sobrenome')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['password2'], 'Repita sua senha')

        for i, value in self.fields.items():
            add_attr(self.fields[i], 'class', 'form-control')
            # if self.fields[i].help_text == '':
            #     add_attr(self.fields[i], 'class', 'mb-3')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]
    first_name = forms.CharField(
        error_messages={'required': 'Digite seu nome.'},
        required=True,
        label='Primeiro Nome'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Digite seu sobrenome.'},
        required=True,
        label='Sobrenome'
    )

    username = forms.CharField(
        label='Nome de Usuário',
        help_text=(
            'O usuário deve possuir letras, números ou esses caracteres @/./+/-/_. '
            'Deve possuir no mínimo 4 e máximo 150 caracteres.'
        ),
        error_messages= {
            'required': 'Esse campo não pode ser vazio.',
            'min_length': 'O nome de usuário deve possuir mais que 4 caracteres.',
            'max_length': 'O nome de usuário deve possuir menos que 150 caracteres.',
        },
        min_length=4, max_length=150,
    )

    email = forms.EmailField(
        error_messages={'required': 'O E-mail é obrigatório'},
        label='E-mail',
        help_text='O e-mail precisa ser válido.'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={'required': 'A senha não por ser vazia.'},
        help_text=('A senha precisa conter pelo menos 8 caracteres'),
        validators=[strong_password],
        label='Senha'
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Confirmar Senha',
        error_messages={
            'required': 'Repita sua senha, por favor!'
        }
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
                'password2': [
                    password_confirmation_error,
                ],
            })