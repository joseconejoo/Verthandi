# Generated by Django 3.0.2 on 2020-04-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0040_sop_notif_mes_fecha_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sop_notif_mes',
            name='fecha_pub',
            field=models.DateTimeField(blank=True),
        ),
    ]