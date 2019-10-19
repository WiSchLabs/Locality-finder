from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import WorldBorder, Category

admin.site.register(WorldBorder, LeafletGeoAdmin)
admin.site.register(Category)
