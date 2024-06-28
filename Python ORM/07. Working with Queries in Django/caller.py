import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review

# Create and check models

# Task 01.Books Finder
def find_book_by_find_books_by_genre_and_language(genre: str, language: str):
    books = Book.objects.filter(genre=genre, language=language)
    return books

# Task 02.Find Authors' Nationalities
def find_authors_nationalities():
    result = []
    # authors = Author.objects.exclude(nationality__isnull=True)
    authors = Author.objects.exclude(nationality=None) 
    # First Way
    for a in authors:
        result.append(f"{a.first_name} {a.last_name} is {a.nationality}")
        
    # Second Way
    # result = [
    #     f"{a.first_name} {a.last_name} is {a.nationality}"
    #     for a in authors
    # ]
        
    return '\n'.join(result)    


# Task 03.Order Books by Year
def order_books_by_year():
    result = []
    books = Book.objects.all().order_by('publication_year', 'title')
    for b in books:
        result.append(f"{b.publication_year} year: {b.title} by {b.author}")
        
    return '\n'.join(result)    


# Task 04.Delete Review by ID
def delete_review_by_id():
    pass


# Task 05.Filter Authors by Nationalities
def filter_authors_by_nationalities():
    pass


# Task 06.Filter Authors by Birth Year
def filter_authors_by_birth_year():
    pass


# Task 07.Change Reviewer's Name
def change_reviewer_name():
    pass


# Run and print your queries