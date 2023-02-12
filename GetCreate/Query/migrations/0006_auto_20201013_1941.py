# Generated by Django 3.1.2 on 2020-10-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]