# Generated by Django 4.0.3 on 2022-11-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_ngapolityrel_is_home_nga'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity',
            name='long_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]