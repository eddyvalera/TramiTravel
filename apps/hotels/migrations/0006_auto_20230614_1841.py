# Generated by Django 3.1 on 2023-06-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_auto_20230614_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='css',
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_adults_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_adults_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_adults_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_childrens_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_childrens_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_childrens_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_childrens_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_childrens_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_infants_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_infants_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_infants_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_infants_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='price_infants_5',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
