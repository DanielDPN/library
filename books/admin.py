from django.contrib import admin
from books.models import Author, Book, Locator, Location

admin.site.register(Author)
admin.site.register(Locator)
admin.site.register(Book)
admin.site.register(Location)
