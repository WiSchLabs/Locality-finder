from django.contrib.gis import forms as geoforms
from leaflet.forms.widgets import LeafletWidget

from main.models import WorldBorder


class WorldBorderCreateForm(geoforms.ModelForm):

    class Meta:
        model = WorldBorder
        exclude = ['worldborder_slug']
        widgets = {
            'mpoly': LeafletWidget()
        }
