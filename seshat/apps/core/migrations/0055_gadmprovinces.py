# Generated by Django 4.0.3 on 2023-12-04 10:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_gadmcountries'),
    ]

    operations = [
        migrations.CreateModel(
            name='GADMProvinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('NAME_1', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_1', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]