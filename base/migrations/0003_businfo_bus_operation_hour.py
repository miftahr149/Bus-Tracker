# Generated by Django 4.2.7 on 2023-11-26 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_busoperationhour'),
    ]

    operations = [
        migrations.AddField(
            model_name='businfo',
            name='bus_operation_hour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.busoperationhour'),
        ),
    ]