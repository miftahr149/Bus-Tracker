# Generated by Django 4.2.7 on 2023-11-27 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_operationhour_end_break_operationhour_start_break_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operationhour',
            options={'ordering': ['start', 'end']},
        ),
    ]