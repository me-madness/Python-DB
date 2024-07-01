import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from typing import List
from helpers import populate_model_with_data
from main_app.models import ArtworkGallery
from main_app.models import Laptop


# Create and check models
def show_highest_rated_art() -> str:
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()
    # SELECT * FROM artwork ORDER BY rating DESC, id ASC LIMIT 1
    
    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"

# print(show_highest_rated_art())


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])
# art1 = ArtworkGallery(
#     art_name="ie2j",
#     artist_name="dido",
#     rating=5,
#     price=0,    
# )
# art2 = ArtworkGallery(
#     art_name="fwfwert",
#     artist_name="mido",
#     rating=6,
#     price=0,
# )

# print(bulk_create_arts())


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()
    # DELETE  FROM artwork WHERE rating < 0

# delete_negative_rated_arts()
  

def show_the_most_expensive_laptop() -> str:
    most_expensive_laptop = Laptop.objects.filter('-price', '-id').first()

    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$"

 
def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args) 
   


def update_to_512_toGB_storage() -> None:
    """
    UPDATE laptop
    SET storage = 512
    WHERE brand in (Asus, Lenovo)
    """
    Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)


def name(args):
 pass


def name(args):
 pass      
# Run and print your queries

# populate_model_with_data(Laptop)