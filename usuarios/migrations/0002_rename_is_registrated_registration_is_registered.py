# Generated by Django 5.0.1 on 2024-01-08 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='is_registrated',
            new_name='is_registered',
        ),
    ]
