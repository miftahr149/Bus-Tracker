# Generated by Django 4.2.7 on 2023-11-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_address_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='get_latlong',
            field=models.BooleanField(default=False, verbose_name='Automatic Get Address'),
        ),
    ]