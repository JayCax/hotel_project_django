from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Client, Room
from .forms import BookingForm


# Create your views here.

def detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, "hotel/detail.html", {"client": client})

def get_rooms(request):
    return render(request, "hotel/list_of_rooms.html", {"rooms": Room.objects.all()})

# BookingForm = modelform_factory(Room, exclude=[])

def new(request):
    if request == "POST":
        # form has been submitted, then process the data
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = BookingForm()
    return render(request, "hotel/new.html", {"form": form})
