# Generated by Django 2.2.2 on 2019-11-25 01:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0006_auto_20191117_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_opci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='datos',
            name='apellido',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el apellido por favor.', regex='^[a-zA-ZñÑ]+$')]),
        ),
        migrations.CreateModel(
            name='P_detal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('p_opci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soporte.P_opci')),
            ],
        ),
    ]
