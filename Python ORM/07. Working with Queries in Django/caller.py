import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review

# Create and check models
def find_book_by_find_books_by_genre_and_language(genre: str, language: str):
    books = Book.objects.filter(genre=genre, language=language)
    return books


def find_authors_nationalities():
    result = []
    authors = Author.objects.exclude(nationality=None)
    for a in authors:
        result.append(f"{a.first_name} {a.last_name} is {a.nationality}")
        
    return '\n'.join(result)    




# Run and print your queries
