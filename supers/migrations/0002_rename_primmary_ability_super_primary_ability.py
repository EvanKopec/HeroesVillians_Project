# Generated by Django 4.0.4 on 2022-05-31 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='primmary_ability',
            new_name='primary_ability',
        ),
    ]
