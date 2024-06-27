import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet
from main_app.models import Artifact
from main_app.models import Location
# from polulate_db_script import populate_model_with_data

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


def create_artifact(name: str, origin: str, age: int, description: str,  is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    
    return f"The artifact {artifact.name} is {artifact.age} years old!"


create_artifact("golden cup", "indiana jones", 2000, "Old", True)


def rename_artifact(artifact: Artifact, new_name: str):
    # First Way
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name) --pk Primary Key
    
    # Second Way
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()
        
   
golden_cup = Artifact.objects.get(pk=1) # SELECT * FROM artifact WHERE id = 1
rename_artifact(golden_cup, "bronze_cup")     


def delete_all_artifacts():
    Artifact.objects.all().delete()
    
 
delete_all_artifacts()   


def show_all_location(name: str, population: str) -> str:
    pass 