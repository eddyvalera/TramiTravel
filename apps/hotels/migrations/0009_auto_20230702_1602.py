# Generated by Django 3.1 on 2023-07-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_auto_20230625_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='cityTo',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='stateTo',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='streetTo',
        ),
    ]
