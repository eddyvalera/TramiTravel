# Generated by Django 3.1 on 2023-09-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]