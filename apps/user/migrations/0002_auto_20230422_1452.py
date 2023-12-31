# Generated by Django 3.1 on 2023-04-22 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('email2', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('phone3', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='agencie')),
                ('revenue', models.FloatField(default=10.0)),
                ('license', models.FileField(blank=True, null=True, upload_to='agencie-license')),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='agencie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agencie', to='user.agencie'),
        ),
    ]
