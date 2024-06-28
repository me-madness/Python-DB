import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from populate_db_script import populate_model_with_data
from django.db.models.query import QuerySet
from main_app.models import Pet
from main_app.models import Artifact
from main_app.models import Location
from main_app.models import Car
from main_app.models import TaskEncoder


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

# create_pet("Boris", "Beast")


def create_artifact(name: str, origin: str, age: int, description: str,  is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    
    return f"The artifact {artifact.name} is {artifact.age} years old!"

# create_artifact("golden cup", "indiana jones", 2000, "Old", True)


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    # First Way
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name) --pk Primary Key
    
    # Second Way
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()
          
# golden_cup = Artifact.objects.get(pk=1) # SELECT * FROM artifact WHERE id = 1
# rename_artifact(golden_cup, "bronze_cup")     


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()
    
# delete_all_artifacts()   


def show_all_location(name: str, population: str) -> str:
    locations = Location.objects.all().order_by('-id') 
    
    return "\n".join(str(l) for l in locations)

# show_all_location()
# populate_model_with_data(Location)

def new_capital() -> None:
    # First Way
    # Location.objects.filter(id=1).update(is_capital=True)
    
    # Second Way
    location = Location.objects.first() # SELECT * FROM locations LIMIT 1
    location.is_capital = True
    location.save()
    
# new_capital()   

 
def get_capital() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')

# get_capital()


def delete_first_location() -> None:
    Location.objects.first().delete()
    
# delete_first_location()  


def apply_discount() -> None:
    cars = Car.objects.all()
    
    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year)) / 100 # 2014 => 2 + 0 + 1 + 4 => 7 / 100 => 0.07
        discount = float(car.price) * percentage_off # 1000 * 0.07 => 70
        car.price_with_discount = float(car.price) - discount # 1000 - 70 => 930
        car.save()
                
# apply_discount()        


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')

# get_recent_cars()


def delete_last_car() -> None:
    Car.objects.last().delete()
    
# delete_last_car()    


def show_unfinished_tasks() -> None:
    pass


def complete_odd_tasks() -> None:
    pass


def encode_and_replace(test: str, task_title: str) -> None:
    pass