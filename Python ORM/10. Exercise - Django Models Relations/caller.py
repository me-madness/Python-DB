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
        
        if not books:
            continue
        
        titles = ", ".join(b.title for b in books)
        authors_with_books.append(
            f"{author.name} has written - {titles}!"
        )
        
    return "\n".join(authors_with_books)    


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()
        

# Task 02 Music App
def add_song_to_artist(artist_name: str, song_title: str) :
    pass


def get_songs_by_artist(artist_name: str):
    pass


def remove_song_from_artist(artist_name: str, song_title: str):
    pass


# Task 03 Shop 
def calculate_average_rating_for_product_by_name(product_name: str):
    pass


def get_reviews_with_high_ratings(threshold: int):
    pass


def get_products_with_no_reviews():
    pass


def delete_products_without_reviews():
    pass  
