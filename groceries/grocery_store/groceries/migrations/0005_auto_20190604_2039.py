# Generated by Django 2.2.1 on 2019-06-04 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0004_groceries_is_availablr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groceries',
            old_name='is_availablr',
            new_name='is_available',
        ),
    ]
