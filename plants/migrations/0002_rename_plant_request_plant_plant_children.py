# Generated by Django 3.2.23 on 2023-11-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='plant_request',
            new_name='plant_children',
        ),
    ]