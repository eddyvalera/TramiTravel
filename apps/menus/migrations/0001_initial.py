# Generated by Django 3.1 on 2023-04-17 13:12

import apps.menus.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField(unique=True)),
                ('tag', models.CharField(max_length=50, unique=True, validators=[apps.menus.validators.validate_tag])),
                ('name_es', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfertGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField(unique=True)),
                ('tag', models.CharField(max_length=50, unique=True, validators=[apps.menus.validators.validate_tag])),
                ('name_es', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('comment_es', models.CharField(max_length=200)),
                ('comment_en', models.CharField(max_length=200)),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=50, unique=True, validators=[apps.menus.validators.validate_tag])),
                ('position', models.IntegerField()),
                ('image', models.ImageField(upload_to='seccion')),
                ('name_es', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('smallDescription_es', ckeditor.fields.RichTextField()),
                ('smallDescription_en', ckeditor.fields.RichTextField()),
                ('description_es', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField()),
                ('actived', models.BooleanField(default=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='menus.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Ofert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=50, unique=True, validators=[apps.menus.validators.validate_tag])),
                ('position', models.IntegerField()),
                ('image', models.ImageField(upload_to='ofert')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='ofert')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='ofert')),
                ('name_es', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('description_es', models.TextField()),
                ('description_en', models.TextField()),
                ('message_es', models.TextField()),
                ('message_en', models.TextField()),
                ('actived', models.BooleanField(default=True)),
                ('ofertGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OfertGroup', to='menus.ofertgroup')),
            ],
        ),
    ]
