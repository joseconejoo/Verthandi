# Generated by Django 3.0.2 on 2020-03-05 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0015_auto_20200220_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='sub_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soporte.P_opci'),
        ),
    ]
