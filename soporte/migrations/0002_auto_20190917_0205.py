# Generated by Django 2.2.2 on 2019-09-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveles',
            name='Nivel',
            field=models.IntegerField(null=True),
        ),
    ]
