# Generated by Django 4.2.7 on 2023-11-27 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_pointeroperationhour_operation_hour_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operationhour',
            options={'ordering': ['end', 'start']},
        ),
    ]
