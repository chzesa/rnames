# Generated by Django 3.2.13 on 2022-06-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rnames_app', '0036_auto_20220603_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalbinning',
            name='binning_scheme',
        ),
        migrations.RemoveField(
            model_name='binning',
            name='binning_scheme',
        ),
    ]