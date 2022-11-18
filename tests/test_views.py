from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve
from project_app.views import home


class ProjectURLsTest(SimpleTestCase):
    "Test the catalogue URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resloves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home)
