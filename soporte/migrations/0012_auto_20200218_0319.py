# Generated by Django 3.0.2 on 2020-02-18 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0011_auto_20200218_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='codigoRe',
        ),
        migrations.AddField(
            model_name='datos',
            name='nivel_usua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.NivelesNum'),
        ),
    ]
