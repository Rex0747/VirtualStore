# Generated by Django 3.0.4 on 2020-04-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0009_auto_20200403_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='porte_pagado',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='precioPorte',
            field=models.FloatField(null=True),
        ),
    ]
