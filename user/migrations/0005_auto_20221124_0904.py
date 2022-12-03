# Generated by Django 3.2 on 2022-11-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221123_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('1', 'active'), ('2', 'deleted')], max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(blank=True, max_length=300, null=True)),
                ('company_address', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('1', 'Admin'), ('2', 'Employee')], default='1', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
    ]