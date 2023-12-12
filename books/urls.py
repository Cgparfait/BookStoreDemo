from django.urls import path
from . views import *


urlpatterns = [
  path('', homeView, name='home'),
  path('book/<int:book_id>', downloadBook, name='download_book'),
]