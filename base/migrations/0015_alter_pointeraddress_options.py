# Generated by Django 4.2.7 on 2023-11-28 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_pointeraddress_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pointeraddress',
            options={'ordering': ['for_bus_route', 'position']},
        ),
    ]
