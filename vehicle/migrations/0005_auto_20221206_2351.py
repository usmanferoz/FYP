# Generated by Django 3.2 on 2022-12-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_vehicle_chassis_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='colour',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='milage',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
