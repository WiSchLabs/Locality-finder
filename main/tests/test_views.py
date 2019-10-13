from django.urls import reverse

from main.tests.test_models import WorldBorderTest


def test_whatever_list_view(self):

    b = WorldBorderTest.create_world_border()
    border_list_url = reverse('main:worldborder_list')
    resp = self.client.get(border_list_url)

    self.assertEqual(resp.status_code, 200)
    self.assertIn(b.name, resp.content)
