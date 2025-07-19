# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # <- Changed this
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <- And this
