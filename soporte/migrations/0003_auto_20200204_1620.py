# Generated by Django 3.0.2 on 2020-02-04 20:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0002_auto_20200204_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_area_nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='datos',
            name='apellido',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el apellido por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='datos',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñáéíóúäëïöüÑàèìòù\\s]+$')]),
        ),
        migrations.AddField(
            model_name='datos',
            name='sub_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.sub_area'),
        ),
    ]
