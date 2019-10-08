from django.contrib.gis import forms as geoforms

from main.models import WorldBorder


class WorldBorderCreateForm(geoforms.ModelForm):

    class Meta:
        model = WorldBorder
        exclude = ['worldborder_slug']
        widgets = {
            'mpoly': geoforms.OSMWidget(attrs={'map_width': 800, 'map_height': 500})
        }
