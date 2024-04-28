from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from hotel.models import Client


# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This is a reminder that this is the John's Hotel: "
                              "Island Paradise Property and NOT City Trekker Property",
                   "guest_count": Client.objects.count(),
                   "clients": Client.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now))

def about_me(request):
    return HttpResponse("Hello everyone! My name is John!")