# Generated by Django 3.0.8 on 2020-08-14 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud_application', '0007_equip_factories'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip',
            name='Factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_application.Factories'),
        ),
    ]