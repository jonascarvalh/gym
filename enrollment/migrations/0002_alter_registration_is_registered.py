# Generated by Django 5.0.2 on 2024-02-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='is_registered',
            field=models.CharField(choices=[('True', 'Matriculado'), ('False', 'Não Matriculado')], max_length=5),
        ),
    ]