# Generated by Django 3.0.5 on 2020-06-22 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soporte', '0049_reset_contra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reset_contra',
            name='usuario_x',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
