from django.shortcuts import render
from django.http import HttpResponse
from .models import Artifact


def artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts/artifacts.html", {"artifacts": artifacts})

def artifact_info(request, artifact_id):
    return render(request, "artifacts/singleartifact.html", {"artifact": Artifact.objects.get(pk=artifact_id)})

def locations(request):
    return HttpResponse("Location Page")

def location_info(request, location_id):
    return HttpResponse("Location info")

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