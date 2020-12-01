from django.contrib import admin

from .models import Artifact, Location

admin.site.site_header = "Awesome Artifacts"
admin.site.site_title = "Totem Admin Area"
admin.site.index_title = "Welcome to the Totem Admin Area"

class LocationInLine(admin.TabularInline):
    model = Location

class ArtifactAdmin(admin.ModelAdmin):
    inlines = [LocationInLine]

admin.site.register(Artifact, ArtifactAdmin)
