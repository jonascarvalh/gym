# Generated by Django 5.0.1 on 2024-01-08 23:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupation', models.CharField(choices=[('Ex', 'Público Externo'), ('E', 'Estudante'), ('F', 'Funcionário')], max_length=2)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('sig_register', models.CharField(max_length=11, unique=True)),
                ('is_registrated', models.BooleanField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
