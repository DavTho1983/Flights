from django.db import models
import datetime

class Flight(models.Model):
    date = models.DateField(default=datetime.date.today)
    dep_time = models.TimeField()
    dep_delay = models.DurationField()
    arr_time = models.TimeField()
    arr_delay = models.DurationField()
    cancelled = models.BooleanField()
    carrier = models.CharField(max_length=3)
    tailnum = models.CharField(max_length=6)
    flight = models.IntegerField()
    origin = models.CharField(max_length=3)
    dest = models.CharField(max_length=3)
    air_time = models.DurationField()
    distance = models.IntegerField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.date} {self.dep_time} {self.dep_delay} {self.arr_time} {self.arr_delay} {self.cancelled} {self.carrier} {self.tailnum} {self.flight} {self.origin} {self.dest} {self.air_time} {self.distance} {self.duration}'
