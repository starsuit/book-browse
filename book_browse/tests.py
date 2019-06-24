from django.test import SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse


class IndexTests(SimpleTestCase):

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_browse/index.html')

    def test_index_renders_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Book Browse</h1>')

    def test_index_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Blah blah blah, incorrect text blah')
