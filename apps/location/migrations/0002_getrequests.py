# Generated by Django 3.1 on 2023-05-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetRequests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('concurrence', models.IntegerField(default=0)),
                ('last_use', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
