# Generated by Django 2.0.9 on 2018-12-21 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rnames_app', '0017_auto_20181221_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='name_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nameone_relation', to='rnames_app.StructuredName'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='name_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nametwo_relation', to='rnames_app.StructuredName'),
        ),
    ]
