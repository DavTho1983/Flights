from django import forms

class FlightForm(forms.Form):
    date = forms.DateField()
    dep_time = forms.TimeField()
    dep_delay = forms.DurationField()
    arr_time = forms.TimeField()
    arr_delay = forms.DurationField()
    cancelled = forms.BooleanField()
    carrier = forms.CharField(max_length=3)
    tailnum = forms.CharField(max_length=6)
    flight = forms.IntegerField()
    origin = forms.CharField(max_length=3)
    dest = forms.CharField(max_length=3)
    air_time = forms.DurationField()
    distance = forms.IntegerField()
    duration = forms.DurationField()
