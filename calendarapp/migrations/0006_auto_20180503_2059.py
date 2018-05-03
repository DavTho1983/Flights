# Generated by Django 2.0.4 on 2018-05-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0005_auto_20180503_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='air_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arr_delay',
            field=models.DurationField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arr_time',
            field=models.TimeField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='cancelled',
            field=models.BooleanField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='carrier',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dep_delay',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dep_time',
            field=models.TimeField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dest',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='distance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.DurationField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='tailnum',
            field=models.IntegerField(max_length=100),
        ),
    ]
