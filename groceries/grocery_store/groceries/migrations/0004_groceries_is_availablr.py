# Generated by Django 2.2.1 on 2019-06-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0003_auto_20190604_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceries',
            name='is_availablr',
            field=models.BooleanField(default=True),
        ),
    ]
