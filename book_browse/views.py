from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from string import Template
import environ
from .forms import BookSearch

env = environ.Env()
env.read_env()  # reading .env file

key = env.str('API_KEY')


def index(request):
    form = BookSearch()
    return render(request, 'book_browse/index.html', {'form': form})


def books(request):

    search = request.GET.get('search', False)
    if search == False:
        return redirect('/')

    queries = {'q': search, 'key': key}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)

    if r.status_code != 200:
        return render(request, 'book_browse/books.html', {'message': 'Sorry, there seems to be an issue with Google Books right now.'})

    data = r.json()

    if not 'items' in data:
        return render(request, 'book_browse/books.html', {'message': 'Sorry, no books match that search term.'})

    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
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
