# Generated by Django 4.0.3 on 2023-10-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_alter_nga_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polity',
            name='polity_tag',
            field=models.CharField(blank=True, choices=[('LEGACY', 'Legacy Polities'), ('POL_AFR_EAST', 'NEW East African Polities'), ('POL_AFR_WEST', 'NEW West African Polities'), ('POL_AFR_SA', 'NEW Southern African Polities'), ('POL_SA_SI', 'NEW South East Indian Polities'), ('CRISISDB_POLITIES', 'CrisisDB-specific Polities'), ('OTHER_TAG', 'Other Polities')], default='OTHER_TAG', max_length=100, null=True),
        ),
    ]