from django.test import SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse


class ErrorTests(SimpleTestCase):

    def test_missing_status_code(self):
        response = self.client.get('/nothing')
        self.assertEquals(response.status_code, 404)


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

    def test_index_renders_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Book Browse</h1>')

    def test_index_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Blah blah blah, incorrect text blah')


class BookListTests(SimpleTestCase):

    def test_books_status_code(self):
        response = self.client.get('/books/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('books'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_browse/books.html')

    def test_books_renders_html(self):
        response = self.client.get('/books/?search=hello+world')
        self.assertContains(response, '<h1>Book Browse</h1>')

    def test_books_does_not_contain_incorrect_html(self):
        response = self.client.get('/books/?search=hello+world')
        self.assertNotContains(
            response, 'Blah blah blah, incorrect text blah')

    def test_books_with_data_renders_list(self):
        response = self.client.get('/books/?search=hello+world')
        self.assertContains(
            response, '<ul')

    def test_books_with_no_results_displays_sorry_message(self):
        response = self.client.get('/books/?search=fghdskfhksdfhsk')
        self.assertContains(
            response, 'Sorry')
