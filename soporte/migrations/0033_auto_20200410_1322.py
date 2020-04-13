# Generated by Django 3.0.2 on 2020-04-10 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0032_auto_20200410_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sop_notif',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')]),
        ),
    ]