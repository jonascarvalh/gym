from django import forms 
from utils.django_forms import add_placeholder, add_attr

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['email'], 'Digite seu e-mail')
        add_placeholder(self.fields['password'], 'Digite sua senha')

        for i, value in self.fields.items():
            add_attr(self.fields[i], 'class', 'form-control')

    email = forms.EmailField(
        label='E-mail:'
    )
    password = forms.CharField(
        label='Senha:',
        widget=forms.PasswordInput()
    )
