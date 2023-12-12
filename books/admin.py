from django.contrib import admin
from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genres', 'publication_date', 'isbn')
    filter_horizontal = ('genre',)

    def display_genres(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])
    display_genres.short_description = 'Genres'





