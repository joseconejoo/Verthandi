# Generated by Django 3.0.2 on 2020-04-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0034_auto_20200410_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='sop_notif',
            name='nombre_e',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='sop_notif',
            name='ubicacion_e',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
