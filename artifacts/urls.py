from django.urls import path
from . import views 

urlpatterns = [
    path("", views.artifacts, name = "artifacts"),
    path("artifacts/<int:artifact_id>/", views.artifact_info, name = "artifact_info"),
    path("locations/", views.locations, name = "locations"),
    path("locations/<int:location_id>/", views.location_info, name = "location_info"),
    path("discovery/<int:year>/", views.discovered_year, name = "discovered_year"),
    path("about", views.about, name = "about"),
    path("discovery/<int:year>/<int:month>/", views.discovered_year_month, name = "discovered_year_month"),
    path("discovery/<int:year>/<int:month>/<int:day>/", views.discovered_year_month_day, name = "discovered_year_month_day"),
]