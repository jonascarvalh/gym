from django.core.exceptions import ValidationError
import re

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

def strong_password(password):
    regex = r'^.{8,}$'
    if not re.match(regex, password):
        raise ValidationError(
            (
                'A senha precisa conter pelo menos 8 caracteres.'
            ),
            code='invalid'
        )
    
def validate_cpf(cpf):
    # Remove non numeric chars
    cpf = ''.join(filter(str.isdigit, cpf))

    # calc first digit checker
    if len(cpf) != 11:
        raise ValidationError(
            ('Digite um CPF válido.'),
            code='invalid'
        )

    # Verify 11 digits
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0

    # if first digit is correct
    if digito1 != int(cpf[9]):
        raise ValidationError(
            ('Digite um CPF válido.'),
            code='invalid'
        )

    # calc second digit checker
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0

    # if second digit is correct
    if digito2 != int(cpf[10]):
        raise ValidationError(
            ('DigiteDigite um CPF válido.'),
            code='invalid'
        )
    
def validade_sig(enrollment):
    if len(enrollment) != 11:
        raise ValidationError(
            ('Digite uma matrícula válida.'),
            code='invalid'
        )