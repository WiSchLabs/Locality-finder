from django.contrib.gis.geos import MultiPolygon
from django.test import TestCase

from main.models import WorldBorder


class WorldBorderTest(TestCase):

    @staticmethod
    def create_world_border(name="border"):
        return WorldBorder.objects.create(
            name=name,
            area=1,
            pop2005=1,
            fips=1,
            iso2=1,
            iso3=1,
            un=1,
            region=1,
            subregion=1,
            lon=1,
            lat=1,

            # GeoDjango-specific: a geometry field (MultiPolygonField)
            mpoly=MultiPolygon()
        )

    def test_world_border_creation(self):
        b = self.create_world_border()
        self.assertTrue(isinstance(b, WorldBorder))
        self.assertEqual(b.worldborder_slug, b.name)
