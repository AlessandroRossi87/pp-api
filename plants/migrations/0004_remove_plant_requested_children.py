# Generated by Django 3.2.23 on 2023-11-30 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_alter_plant_taxonomy_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='requested_children',
        ),
    ]
