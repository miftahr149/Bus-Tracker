# Generated by Django 4.2.7 on 2023-11-28 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_pointeraddress_remove_startroute_route_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busroute',
            options={'ordering': ['type_bus']},
        ),
    ]