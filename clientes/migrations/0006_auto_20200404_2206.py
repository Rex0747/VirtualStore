# Generated by Django 3.0.4 on 2020-04-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200404_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='nombreCliente',
            field=models.CharField(max_length=40),
        ),
    ]
