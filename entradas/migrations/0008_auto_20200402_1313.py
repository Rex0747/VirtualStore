# Generated by Django 3.0.5 on 2020-04-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0007_auto_20200402_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='agencia',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
