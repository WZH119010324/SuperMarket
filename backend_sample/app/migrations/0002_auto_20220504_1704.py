# Generated by Django 3.2.13 on 2022-05-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='City',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.AddField(
            model_name='address',
            name='Country',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.AddField(
            model_name='address',
            name='Region',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.AddField(
            model_name='address',
            name='State',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.AlterField(
            model_name='address',
            name='PostalCode',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='address',
            name='Segment',
            field=models.CharField(default='null', max_length=32),
        ),
    ]
