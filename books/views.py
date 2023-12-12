
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

from django.shortcuts import render

from .models import *

def homeView(request):
  books=Book.objects.all()
  context={
    "books":books,
  }
  return render(request, 'books/home.html', context)


def downloadBook(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  file_path = book.book_file.path
  
  file_wrapper = FileWrapper(open(file_path, 'rb'))
  mime_type, _ = mimetypes.guess_type(file_path)
  response = HttpResponse(file_wrapper, content_type=mime_type)
  response['Content-Length'] = os.path.getsize(file_path)
  response['Content-Disposition'] = 'attachment; filename="%s"' % book.book_file.name
  return response