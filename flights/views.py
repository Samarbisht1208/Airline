from django.shortcuts import render

from .models import Flight, Passenger

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
    "flights_list": Flight.objects.all()
    })

def flight(request, flight_ki_id):
    #here pk means primary key (id can also work)
    try:
        flight_variable = Flight.objects.get(pk = flight_ki_id)
        return render(request, "flights/flight.html", {
            "flight_placeholder": flight_variable,
            "passengers_placeholder": flight_variable.passengers_ye_rhe.all(),
            "non_passengers_placeholder": Passenger.objects.exclude(flights=flight_variable).all()  
        })
    except Flight.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    


def book(request, flight_ki_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_ki_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger_field"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight_name", args=(flight.id,)))