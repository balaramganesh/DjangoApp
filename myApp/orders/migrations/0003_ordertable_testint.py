# Generated by Django 4.1.13 on 2024-05-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_ordertable_testint'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertable',
            name='testInt',
            field=models.IntegerField(default=5),
        ),
    ]
