from django.shortcuts import render
from .models import Flight

def index(request):

    flights = Flight.objects.all()[:5]

    return render(request, 'calendarapp/index.html', {'flights': flights})

def details(request, pk):

    flight = Flight.objects.get(id=pk)

    return render(request, 'calendarapp/details.html', {'flight': flight})
