import django_filters
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "authors"


class Locator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "locators"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    locators = models.ManyToManyField(Locator)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"


class Location(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    locator = models.ForeignKey(Locator, on_delete=models.CASCADE)

    class Meta:
        db_table = "locations"


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', ]
