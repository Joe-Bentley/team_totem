from django.contrib import admin

from .models import Artifact, Location

admin.site.site_header = "Awesome Artifacts"
admin.site.site_title = "Totem Admin Area"
admin.site.index_title = "Welcome to the Totem Admin Area"

class ArtifactInLine(admin.TabularInline):
    model = Artifact

class LocationAdmin(admin.ModelAdmin):
    inlines = [ArtifactInLine]

admin.site.register(Artifact)

admin.site.register(Location, LocationAdmin)
