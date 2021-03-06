# Generated by Django 3.0.8 on 2020-08-08 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crud_application', '0004_auto_20200808_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturantName', models.CharField(max_length=50)),
                ('startCount', models.IntegerField(blank=True, max_length=5)),
                ('managerFullName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetName', models.CharField(max_length=50)),
                ('cityName', models.CharField(max_length=50)),
                ('countryName', models.CharField(max_length=50)),
                ('fullAddress', models.CharField(max_length=50)),
                ('resturantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_application.Resturant')),
            ],
        ),
    ]
