from django import forms


class BookSearch(forms.Form):
    search = forms.CharField(
        label="Search for a book", required=False, widget=forms.TextInput(attrs={'class': "field__input", 'id': 'search', 'autofocus': True}))
    author = forms.CharField(
        label="Search for an author", required=False, widget=forms.TextInput(attrs={'class': "field__input", 'id': 'author'}))
