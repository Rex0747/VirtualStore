# Generated by Django 3.0.4 on 2020-03-29 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('cp', models.CharField(max_length=5, null=True)),
                ('telefono', models.CharField(max_length=9, null=True)),
                ('movil', models.CharField(max_length=9, null=True)),
                ('mail', models.EmailField(max_length=60, null=True, unique=True)),
                ('fecha_alta', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
