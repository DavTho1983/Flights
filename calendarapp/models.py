from django.db import models

# year,month,day,dep_time,dep_delay,arr_time,arr_delay,cancelled,
# carrier,tailnum,flight,origin,dest,air_time,distance,hour,min

class Flight(models.Model):
    date = models.DateField(max_length=100)
    dep_time = models.TimeField(max_length=100)
    dep_delay = models.CharField(max_length=100)
    arr_time = models.TimeField(max_length=100)
    arr_delay = models.DurationField(max_length=100)
    cancelled = models.BooleanField(max_length=100)
    carrier = models.CharField(max_length=100)
    tailnum = models.IntegerField(max_length=100)
    flight = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    air_time = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    duration = models.DurationField(max_length=100)

    def __str__(self):
        return f'{self.flight} {self.dest} {self.year} {self.month} {self.day}'
