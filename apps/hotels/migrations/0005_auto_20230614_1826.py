# Generated by Django 3.1 on 2023-06-14 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_flight_packagesonly'),
        ('hotels', '0004_auto_20230614_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('room_space', models.IntegerField(default=0)),
                ('maxChildrens', models.IntegerField(default=0)),
                ('maxInfants', models.IntegerField(default=0)),
                ('maxAdults', models.IntegerField(default=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='isForAdults',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='maxAdults',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='maxChildrens',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='maxInfants',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='airline',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='arrival_flight',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='arrival_flight_return',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='departure_flight',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='departure_flight_return',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='vacationpackage',
            name='room_type',
        ),
        migrations.AddField(
            model_name='vacationpackage',
            name='flightBegin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FlightBegin', to='reservations.flight'),
        ),
        migrations.AddField(
            model_name='vacationpackage',
            name='flightReturn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FlightReturn', to='reservations.flight'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='reservations.destinatation'),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacationpackage',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='reservations.destinatation'),
        ),
        migrations.DeleteModel(
            name='Destinatation',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotels.hotel'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='hotels.roomtype'),
        ),
        migrations.AddField(
            model_name='vacationpackage',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Room', to='hotels.room'),
            preserve_default=False,
        ),
    ]
