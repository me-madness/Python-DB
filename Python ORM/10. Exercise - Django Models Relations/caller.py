import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author, Book


# Create queries within functions

def show_all_authors_with_their_books() -> str:
    authors_with_books = []
    
    authors = Author.objects.all().order_by("id") # select prefetch  prefetch_related
    
    for author in authors:
        books = Book.objects.filter(author=author)
        # books = author.book_set.all() # Option 2
        
    return "\n".join(authors_with_books)    