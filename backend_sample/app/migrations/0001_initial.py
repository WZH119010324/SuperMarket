# Generated by Django 3.2.13 on 2022-05-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostalCode', models.IntegerField()),
                ('Segment', models.CharField(max_length=32)),
            ],
        ),
    ]
