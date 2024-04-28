from django.shortcuts import render, get_object_or_404

from .models import Room, Client

# Create your views here.

def detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, "hotel/detail.html", {"client": client})