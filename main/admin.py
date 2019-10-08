from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import WorldBorder


admin.site.register(WorldBorder, LeafletGeoAdmin)
