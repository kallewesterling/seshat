# Generated by Django 4.0.3 on 2024-04-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_seshatprivatecomment_seshatprivatecommentpart'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity',
            name='private_comment_n',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.seshatprivatecomment'),
        ),
    ]
