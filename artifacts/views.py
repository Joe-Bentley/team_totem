from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def artifacts(request):
    return HttpResponse("Artifact Page")

def artifact_info(request, artifact_id):
    return HttpResponse("Detail Page")

def locations(request):
    return HttpResponse("Location Page")

def location_info(request, location_id):
    return HttpResponse("Location info")

def discovered_year(request, year):
    return HttpResponse("Year Discovered")

def discovered_year_month(request, year, month):
    return HttpResponse("Year/Month Discovered")

def discovered_year_month_day(request, year, month, day):
    return HttpResponse("Year/Month/Day Discovered")