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

    string = 'world'

    queries = {'q': string, 'key': key}
# r seems to be the convention
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)

    books = r.json()['items']

    return render(request, 'book_browse/books.html', {'books': books})
