# Generated by Django 4.2.7 on 2023-11-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusOperationHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_bus', models.CharField(max_length=3)),
                ('operation_hour_rel', models.ManyToManyField(to='base.operationhour')),
            ],
        ),
    ]
