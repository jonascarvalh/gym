# from inspect import signature
from random import randint
from faker import Faker
import random

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


ocupations = ['E', 'F', 'Ex']

def make_registration():
    return {
        'name': fake.name(),
        'cpf': fake.random_number(digits=11, fix_len=True),
        'sig_register': fake.random_number(digits=11, fix_len=True),
        'ocupation': random.choice(ocupations),
        'is_registered': random.choice(['True', 'False'])
    }