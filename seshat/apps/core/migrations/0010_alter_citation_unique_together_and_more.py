# Generated by Django 4.0.3 on 2022-08-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_citation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='citation',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='citation',
            constraint=models.UniqueConstraint(fields=('ref', 'page_from', 'page_to'), name='No_PAGE_TO_OR_FROM'),
        ),
        migrations.AddConstraint(
            model_name='citation',
            constraint=models.UniqueConstraint(condition=models.Q(('page_from__isnull', True)), fields=('ref', 'page_from'), name='No_PAGE_FROM'),
        ),
        migrations.AddConstraint(
            model_name='citation',
            constraint=models.UniqueConstraint(condition=models.Q(('page_to__isnull', True)), fields=('ref', 'page_to'), name='No_PAGE_TO'),
        ),
    ]
