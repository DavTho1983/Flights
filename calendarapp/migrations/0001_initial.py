# Generated by Django 2.0.4 on 2018-05-04 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('dep_time', models.TimeField()),
                ('dep_delay', models.DurationField()),
                ('arr_time', models.TimeField()),
                ('arr_delay', models.DurationField()),
                ('cancelled', models.BooleanField()),
                ('carrier', models.CharField(max_length=3)),
                ('tailnum', models.CharField(max_length=6)),
                ('flight', models.IntegerField()),
                ('origin', models.CharField(max_length=3)),
                ('dest', models.CharField(max_length=3)),
                ('air_time', models.DurationField()),
                ('distance', models.IntegerField()),
                ('duration', models.DurationField()),
            ],
        ),
    ]
