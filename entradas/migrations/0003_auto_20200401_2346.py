# Generated by Django 3.0.4 on 2020-04-01 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_auto_20200401_2340'),
        ('entradas', '0002_auto_20200401_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='fk_articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articulos.articulos'),
        ),
    ]
