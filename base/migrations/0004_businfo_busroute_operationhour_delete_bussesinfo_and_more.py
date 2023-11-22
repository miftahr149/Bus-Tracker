# Generated by Django 4.2.7 on 2023-11-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_address_get_latlong'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_bus', models.CharField(max_length=3)),
                ('route', models.ManyToManyField(to='base.address')),
            ],
        ),
        migrations.CreateModel(
            name='OperationHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=3)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='BussesInfo',
        ),
        migrations.AddField(
            model_name='businfo',
            name='bus_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.busroute'),
        ),
        migrations.AddField(
            model_name='businfo',
            name='operation_hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.operationhour'),
        ),
    ]
