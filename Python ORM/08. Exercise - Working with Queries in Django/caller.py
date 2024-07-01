import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.choices import LaptopBrandChoice, OperationSystemChoice
from django.db.models import Case, Value, When
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


def update_to_16_GB_memory() -> None:
    # First Way
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)
    
    # Second Way
    


def update_operation_systems() -> None:
    # Solution One
    Laptop.objects.filter(brand="Asus").update(operation_systems=OperationSystemChoice.WINDOWS)
    Laptop.objects.filter(brand="Apple").update(operation_systems=OperationSystemChoice.MACOS)
    Laptop.objects.filter(brand="Apple").update(operation_systems=OperationSystemChoice.MACOS)
    Laptop.objects.filter(brand__in=("Dell", "Acer")).update(operation_systems=OperationSystemChoice.LINUX)
    Laptop.objects.filter(brand="Lenovo").update(operation_systems=OperationSystemChoice.CHROME_OS)

    # Solution Two
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(operation_system=OperationSystemChoice.WINDOWS)),
            When(brand="Apple",then=Value(operation_systems=OperationSystemChoice.MACOS)),
            When(brand__in=("Dell", "Acer"), then=Value(operation_systems=OperationSystemChoice.LINUX)),
            When(brand="Lenovo", then=Value(operation_systems=OperationSystemChoice.CHROME_OS))
        )
    )

def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# Run and print your queries

# populate_model_with_data(Laptop)