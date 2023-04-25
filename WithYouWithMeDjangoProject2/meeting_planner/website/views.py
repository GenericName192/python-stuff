from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting, Room

def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This is a message from another page :o",
                   "meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("the time is: " + str(datetime.now()))

def about(request):
    return HttpResponse("I am David I am learning python and I am pretty great!")