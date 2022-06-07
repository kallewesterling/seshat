# Generated by Django 4.0.3 on 2022-05-24 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reference_long_name_alter_reference_title'),
        ('crisisdb', '0008_alter_rate_of_return_rate_of_return'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='total_revenue',
            name='section',
        ),
        migrations.AlterField(
            model_name='annual_wages',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='balance',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='diding_taxes',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='disease_event',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='famine_event',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='gdp_growth_rate',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='gdp_per_capita',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='gdp_total',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='jinshi_degrees_awarded',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='land_taxes_collected',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='land_yield',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='lijin',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='maritime_custom',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='misc_incomes',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='other_incomes',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='population',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='rate_of_gdp_per_capita_growth',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='rate_of_return',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='revenue_official',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='revenue_real',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='salt_tax',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='shares_of_world_gdp',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='taiping_rebellion',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='tariff_and_transit',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='total_economic_output',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='total_expenditure',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='total_revenue',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='total_tax',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='wages',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AlterField(
            model_name='worker_wage',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
    ]