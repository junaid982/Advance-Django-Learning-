# Generated by Django 3.1.2 on 2020-10-10 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CheeseQuery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='origin',
            new_name='place',
        ),
    ]
