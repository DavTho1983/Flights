# Generated by Django 2.0.4 on 2018-05-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_flight_dep_delay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='day',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='min',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='month',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='year',
        ),
        migrations.AddField(
            model_name='flight',
            name='date',
            field=models.DateField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='flight',
            name='duration',
            field=models.DurationField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arr_delay',
            field=models.DurationField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arr_time',
            field=models.TimeField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='cancelled',
            field=models.BooleanField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dep_time',
            field=models.TimeField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='tailnum',
            field=models.IntegerField(default='', max_length=100),
        ),
    ]
