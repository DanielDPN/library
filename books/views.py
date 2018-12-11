from django.shortcuts import redirect, render, get_object_or_404

from .forms import BookForm, LocationForm
from .models import Book, Location, BookFilter


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location/location_list.html', {'locations': locations})


def location_detail(request, pk):
    loc = get_object_or_404(Location, pk=pk)
    return render(request, 'location/location_detail.html', {'loc': loc})


def location_new(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            loc = form.save(commit=False)
            loc.save()
            return redirect('location_detail', pk=loc.pk)
    else:
        form = LocationForm()
    return render(request, 'location/location_edit.html', {'form': form})


def location_edit(request, pk):
    loc = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=loc)
        if form.is_valid():
            loc = form.save(commit=False)
            loc.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=loc)
    return render(request, 'location/location_edit.html', {'form': form})
