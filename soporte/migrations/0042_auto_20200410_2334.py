# Generated by Django 3.0.2 on 2020-04-11 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0041_auto_20200410_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sop_notif_mes',
            name='sop_notif_tick',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.sop_notif'),
        ),
    ]