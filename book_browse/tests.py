from django.test import SimpleTestCase
from django.http import HttpRequest

class IndexTests(SimpleTestCase):

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

# Create your tests here.
