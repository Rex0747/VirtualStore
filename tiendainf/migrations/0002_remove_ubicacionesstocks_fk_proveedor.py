# Generated by Django 3.0.4 on 2020-04-05 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendainf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacionesstocks',
            name='fk_proveedor',
        ),
    ]