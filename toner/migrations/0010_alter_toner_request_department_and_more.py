# Generated by Django 5.0.1 on 2024-01-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toner', '0009_kenindia_department_kenindia_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toner_request',
            name='Department',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='toner_request',
            name='Location',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='toner_request',
            name='Toner_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='toner_request',
            name='printer_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]