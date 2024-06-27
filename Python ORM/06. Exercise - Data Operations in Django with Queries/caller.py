import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet
from polulate_db_script import populate_model_with_data

# Create queries within functions
def create_pet(name: str, species: str) -> str:
    # First Way
    pet = Pet.objects.create(
        name=name,
        species=species,
    )
    
    # Second Way
    # pet = Pet(name=name, species=species)
    # pet.save()
    
    return f"{pet.name} is a very cute {pet.species}!"


create_pet("Boris", "Beast")