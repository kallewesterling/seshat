# Generated by Django 4.0.3 on 2024-06-20 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seshat_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]