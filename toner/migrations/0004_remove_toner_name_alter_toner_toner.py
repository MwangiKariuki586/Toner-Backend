# Generated by Django 5.0.1 on 2024-01-11 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toner', '0003_toner_toner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toner',
            name='name',
        ),
        migrations.AlterField(
            model_name='toner',
            name='Toner',
            field=models.CharField(default='', max_length=500),
        ),
    ]
