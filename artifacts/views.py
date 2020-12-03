from django.shortcuts import render
from django.http import HttpResponse
from .models import Artifact, Location


def artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts/artifacts.html", {"artifacts": artifacts})

def artifact_info(request, artifact_id):
    return render(request, "artifacts/singleartifact.html", {"artifact": Artifact.objects.get(pk=artifact_id), "host_prefix": request.get_host()})

def locations(request):
    locations = Location.objects.all()
    return render(request, "artifacts/locations.html", {"locations": locations, "host_prefix": request.get_host()})

def location_info(request, location_id):
    shared_location = Location.objects.get(pk=location_id)
    all_artifacts = Artifact.objects.filter(location = shared_location)
    return render (
        request, 
        "artifacts/singlelocation.html", 
        {"artifacts": all_artifacts, "location": shared_location, "host_prefix": request.get_host()} 
    )

def discovered_year(request, year):
    artifacts = Artifact.objects.filter(pub_date__year=year)
    return render(
        request,
        "artifacts/discovered.html",
        {"artifacts": artifacts, "date": year}
    )

def discovered_year_month(request, year, month):
    return HttpResponse("Year/Month Discovered")

def discovered_year_month_day(request, year, month, day):
    return HttpResponse("Year/Month/Day Discovered")