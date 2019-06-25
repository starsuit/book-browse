from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import requests
from string import Template
import environ

env = environ.Env()
env.read_env()  # reading .env file

key = env.str('API_KEY')


def index(request):

    return render(request, 'book_browse/index.html', {})


def books(request):

    search = request.GET.get('search', False)

    queries = {'q': search, 'key': key}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)

    data = r.json()

    if not 'items' in data:
        return render(request, 'book_browse/books.html', {})

    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'],
            'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
            'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
            'info': book['volumeInfo']['infoLink'],
            'popularity': book['volumeInfo']['ratingsCount'] if 'ratingsCount' in book['volumeInfo'] else 0
        }
        books.append(book_dict)

    def sort_by_pop(e):
        return e['popularity']

    books.sort(reverse=True, key=sort_by_pop)

    return render(request, 'book_browse/books.html', {'books': books})
