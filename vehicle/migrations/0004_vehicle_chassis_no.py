# Generated by Django 3.2 on 2022-12-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicleallocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='chassis_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
