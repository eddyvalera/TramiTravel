# Generated by Django 3.1 on 2023-06-10 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('nameCode', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='package_airline')),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('zelle', models.CharField(blank=True, max_length=100, null=True)),
                ('zelle_owner', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(blank=True, default=None, null=True)),
                ('amount', models.FloatField(default=0)),
                ('revenue', models.FloatField(default=0)),
                ('liquidated', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Destinatation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('cityCode', models.CharField(max_length=3)),
                ('countryCode', models.CharField(max_length=3)),
                ('begin', models.BooleanField(default=True)),
                ('destination', models.BooleanField(default=True)),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='package_hotel')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('maxChildrens', models.IntegerField(default=0)),
                ('maxInfants', models.IntegerField(default=0)),
                ('maxAdults', models.IntegerField(default=2)),
                ('isForAdults', models.BooleanField(default=True)),
                ('actived', models.BooleanField(default=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='hotels.destinatation')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('css', models.TextField(blank=True, null=True)),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('nameCode', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='package_transport')),
                ('actived', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacationPackage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startDate', models.DateField()),
                ('lastDate', models.DateField()),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price_adults_1', models.FloatField(default=0.0)),
                ('price_adults_2', models.FloatField(default=0.0)),
                ('price_adults_3', models.FloatField(default=0.0)),
                ('price_adults_4', models.FloatField(default=0.0)),
                ('price_adults_5', models.FloatField(default=0.0)),
                ('price_childrens_1', models.FloatField(default=0.0)),
                ('price_childrens_2', models.FloatField(default=0.0)),
                ('price_childrens_3', models.FloatField(default=0.0)),
                ('price_childrens_4', models.FloatField(default=0.0)),
                ('price_childrens_5', models.FloatField(default=0.0)),
                ('price_infants_1', models.FloatField(default=0.0)),
                ('price_infants_2', models.FloatField(default=0.0)),
                ('price_infants_3', models.FloatField(default=0.0)),
                ('price_infants_4', models.FloatField(default=0.0)),
                ('price_infants_5', models.FloatField(default=0.0)),
                ('taxes', models.FloatField(default=0.0)),
                ('flight', models.FloatField(default=0.0)),
                ('transfer', models.FloatField(default=0.0)),
                ('markup', models.FloatField(default=0.0)),
                ('servicesInclude', models.CharField(blank=True, max_length=100, null=True)),
                ('accommodation', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_flight', models.DateTimeField()),
                ('arrival_flight', models.DateTimeField()),
                ('departure_traslate', models.DateTimeField()),
                ('arrival_traslate', models.DateTimeField()),
                ('actived', models.BooleanField(default=True)),
                ('airline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.airline')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotels.hotel')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='hotels.destinatation')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='hotels.roomtype')),
                ('transport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.transport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(blank=True, max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100)),
                ('motherLastName', models.CharField(blank=True, max_length=100, null=True)),
                ('birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('imageDocument', models.ImageField(blank=True, null=True, upload_to='package-booking-document')),
                ('documentNumber', models.CharField(max_length=14)),
                ('documentExpiration', models.DateField()),
                ('documentType', models.CharField(max_length=50)),
                ('documentCountry', models.CharField(max_length=50)),
                ('imageSecondaryDocument', models.ImageField(blank=True, null=True, upload_to='package-booking-document')),
                ('secondaryDocumentNumber', models.CharField(blank=True, max_length=14, null=True)),
                ('secondaryDocumentExpiration', models.DateField(blank=True, null=True)),
                ('secondaryDocumentType', models.CharField(blank=True, max_length=50, null=True)),
                ('secondaryDocumentCountry', models.CharField(blank=True, max_length=50, null=True)),
                ('streetBegin', models.CharField(max_length=200)),
                ('cityBegin', models.CharField(max_length=100)),
                ('stateBegin', models.CharField(max_length=100)),
                ('streetTo', models.CharField(max_length=200)),
                ('cityTo', models.CharField(max_length=100)),
                ('stateTo', models.CharField(max_length=100)),
                ('reservationCode', models.BigIntegerField()),
                ('pnr', models.CharField(blank=True, max_length=50, null=True)),
                ('pnr_return', models.CharField(blank=True, max_length=50, null=True)),
                ('license', models.CharField(blank=True, max_length=100, null=True)),
                ('actived', models.BooleanField(default=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_bill', to='hotels.bill')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VacationPackage', to='hotels.vacationpackage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
