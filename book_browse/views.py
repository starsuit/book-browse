from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import requests
from string import Template
import environ

env = environ.Env()
env.read_env()  # reading .env file


def index(request):

    string = 'world'
    key = env.str('API_KEY')

    queries = {'q': string, 'key': key}
# r seems to be the convention
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)

    books = r.json()['items']

    return render(request, 'book_browse/index.html', {'books': books})
