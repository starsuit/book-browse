from django import forms


class BookSearch(forms.Form):
    search = forms.CharField(
        label="Search for a book", widget=forms.TextInput(attrs={'class': "field__input", 'id': 'search', 'autofocus': True}))
