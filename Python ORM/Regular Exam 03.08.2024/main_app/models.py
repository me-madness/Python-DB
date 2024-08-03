from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator 
from validators import OnlyDigitsValidator
# Create your models here.


class DateTime(models.Model):
    class Meta:
        abstract = True
        
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )    
        
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )
   

class Astronaut(DateTime):
    
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            OnlyDigitsValidator()
        ]
    )
    
    is_active = models.BooleanField(
        default=True,
    )
    
    date_of_birth = models.DateField(
        null=False,
        blank=False,
    )
    
    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    
   
class Spacecraft(DateTime):   
    
    manufacturer = models.CharField(
        max_length=100,
    )
    
    capacity = models.SmallIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    
    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )
    
    launch_date = models.DateField()
    

class Mission(DateTime):
    
    description = models.TextField(
        null=False,
        blank=False,
    )
    
    status = models.CharField(
        max_length=9,
        default="Planned",
        validators=[
            #valid choices = "Planned", "Ongoing", "Completed"
        ]
        
    )
    
    launch_date = models.DateField()
    
    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
    )
    
    astronauts = models.ForeignKey(
        to=Astronaut,
    )
    
    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )