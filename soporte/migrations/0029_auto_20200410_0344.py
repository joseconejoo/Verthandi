# Generated by Django 3.0.2 on 2020-04-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0028_auto_20200409_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sop_notif',
            name='num_pc',
            field=models.CharField(max_length=90),
        ),
    ]
