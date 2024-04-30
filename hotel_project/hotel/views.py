from django.shortcuts import render, get_object_or_404

from .models import Client, Room


# Create your views here.

def detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, "hotel/detail.html", {"client": client})

def get_rooms(request):
    return render(request, "hotel/list_of_rooms.html", {"rooms": Room.objects.all()})