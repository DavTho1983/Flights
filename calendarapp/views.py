from django.shortcuts import render
from .models import Flight
from django.http import HttpResponseRedirect
from .forms import FlightForm

def index(request):

    flights = Flight.objects.all()[5:]

    return render(request, 'calendarapp/index.html', {'flights': flights})

def details(request, pk):

    flight = Flight.objects.get(id=pk)

    return render(request, 'calendarapp/details.html', {'flight': flight})

def add(request):

    if request.method == 'POST':
        form = FlightForm(request.POST)

        if form.is_valid():

            date = form.cleaned_data['date']
            dep_time = form.cleaned_data['dep_time']
            dep_delay = form.cleaned_data['dep_delay']
            arr_time = form.cleaned_data['arr_time']
            arr_delay = form.cleaned_data['arr_delay']
            cancelled = form.cleaned_data['cancelled']
            carrier = form.cleaned_data['carrier']
            tailnum = form.cleaned_data['tailnum']
            flight = form.cleaned_data['flight']
            origin = form.cleaned_data['origin']
            dest = form.cleaned_data['dest']
            air_time = form.cleaned_data['air_time']
            distance = form.cleaned_data['distance']
            duration = form.cleaned_data['duration']

            Flight.objects.create(
                date = date,
                dep_time = dep_time,
                dep_delay = dep_delay,
                arr_time = arr_time,
                arr_delay = arr_delay,
                cancelled = cancelled,
                carrier = carrier,
                tailnum = tailnum,
                flight = flight,
                origin = origin,
                dest = dest,
                air_time = air_time,
                distance = distance,
                duration = duration,
            ).save()

            return HttpResponseRedirect('/')

    else:
        form = FlightForm()

    return render(request, 'calendarapp/form.html', {'form': form})
