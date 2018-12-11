from django import forms

from .models import Book, Location


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'summary', 'author', )


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('locator', 'book', )
