from django.shortcuts import render
from .models import Flight

def index(request):

    flights = Flight.objects.all()[:5]

    return render(request, 'calendarapp/index.html', {'flights': flights})
