from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator 
from validators import OnlyDigitsValidator
# Create your models here.

class Astronaut(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )
    
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
    
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )
   
   
class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )    
    
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
    
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )


class Mission(models.Model):
    