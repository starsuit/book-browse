from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import requests
from string import Template


def index(request):

    string = 'world'

    queries = {'q': string}
# r seems to be the convention
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)

    books = r.json()['items']

    return render(request, 'book_browse/index.html', {'books': books})
    # return HttpResponse('Hello world')
