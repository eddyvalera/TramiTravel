# Generated by Django 3.1 on 2023-07-16 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_auto_20230716_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='clients',
        ),
        migrations.AddField(
            model_name='client',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotels.booking'),
            preserve_default=False,
        ),
    ]
