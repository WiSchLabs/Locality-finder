from django.test import TestCase

from main.forms import WorldBorderCreateForm
from main.tests.test_models import WorldBorderTest


class WorldBorderFormTest(TestCase):

    def test_valid_form(self):
        b = WorldBorderTest.create_world_border(name="border1")

        data = dict()
        data['name'] = b.name
        data['area'] = b.area
        data['pop2005'] = b.pop2005
        data['fips'] = b.fips
        data['iso2'] = b.iso2
        data['iso3'] = b.iso3
        data['un'] = b.un
        data['region'] = b.region
        data['subregion'] = b.subregion
        data['lon'] = b.lon
        data['lat'] = b.lat
        data['mpoly'] = b.mpoly

        form = WorldBorderCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        b = WorldBorderTest.create_world_border(name="border1")

        data = dict()
        data['name'] = b.name
        # missing other params

        form = WorldBorderCreateForm(data=data)
        self.assertFalse(form.is_valid())
