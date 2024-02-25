# Generated by Django 5.0.2 on 2024-02-25 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrollment', '0002_alter_registration_is_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('imc', models.FloatField()),
                ('is_evaluated', models.CharField(choices=[('True', 'Avaliado'), ('False', 'Não Avaliado')], max_length=5)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enrollment.registration')),
            ],
        ),
    ]