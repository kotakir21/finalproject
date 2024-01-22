# Generated by Django 4.2.9 on 2024-01-22 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictsme', '0002_rename_is_assigned_to_engineer_ictsme_is_assigned_to_officer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ictsme',
            name='hub_requirements',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ictsme',
            name='mentor_support',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ictsme',
            name='ura_registration_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ictsme',
            name='ursb_registration_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ictsme',
            name='year_of_incorporation',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
