# Generated by Django 4.1.3 on 2022-11-18 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0002_super_catchphrase_super_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
        ),
    ]
