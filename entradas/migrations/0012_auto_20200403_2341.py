# Generated by Django 3.0.4 on 2020-04-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0011_auto_20200403_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='agencia',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='precioPorte',
            field=models.FloatField(default=True, null=True),
        ),
    ]
