from django.db import models

# year,month,day,dep_time,dep_delay,arr_time,arr_delay,cancelled,
# carrier,tailnum,flight,origin,dest,air_time,distance,hour,min

class Flight(models.Model):
    year = models.CharField(max_length=100, default='')
    month = models.CharField(max_length=100, default='')
    day = models.CharField(max_length=100, default='')
    dep_time = models.CharField(max_length=100, default='')
    dep_delay = models.CharField(max_length=100, default='')
    arr_time = models.CharField(max_length=100, default='')
    arr_delay = models.CharField(max_length=100, default='')
    cancelled = models.CharField(max_length=100, default='')
    carrier = models.CharField(max_length=100, default='')
    tailnum = models.CharField(max_length=100, default='')
    flight = models.CharField(max_length=100, default='')
    origin = models.CharField(max_length=100, default='')
    dest = models.CharField(max_length=100, default='')
    air_time = models.CharField(max_length=100, default='')
    distance = models.CharField(max_length=100, default='')
    hour = models.CharField(max_length=100, default='')
    min = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.flight} {self.dest} {self.year} {self.month} {self.day}'
