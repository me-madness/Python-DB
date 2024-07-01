import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from helpers import populate_model_with_data
from main_app.models import ArtworkGallery


# Create and check models
def show_highest_rated_art() -> str:
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()
    # SELECT * FROM artwork ORDER BY rating DESC, id ASC LIMIT 1
    
    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"

# print(show_highest_rated_art())


def bulk_create_arts(first_art, second_art):
    pass


def delete_negative_rated_arts():
    pass

  
# Run and print your queries

populate_model_with_data(ArtworkGallery, 20)