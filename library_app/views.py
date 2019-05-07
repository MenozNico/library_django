from .models import Author, Book

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class AutoreDetailCBV(DetailView):
    model = Author
    template_name = "author.html"

class BookListCBV(ListView):
    model = Book
    templates_name = "books.html"

