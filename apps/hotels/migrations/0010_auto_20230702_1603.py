# Generated by Django 3.1 on 2023-07-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20230702_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='liquidated',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='markup',
            field=models.FloatField(default=0),
        ),
    ]
