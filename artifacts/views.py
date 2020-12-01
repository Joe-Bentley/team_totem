from django.shortcuts import render
from django.http import HttpResponse
from .models import Artifact

# Create your views here.

def artifacts(request):
    artifacts = Artifact.objects.all()
    arts = ", ".join([a.text for a in artifacts])
    return HttpResponse(arts)

def artifact_info(request, artifact_id):
    a = Artifact.objects.get(pk=artifact_id)
    return HttpResponse(a.info)

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