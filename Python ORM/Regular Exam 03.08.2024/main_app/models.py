from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator 
from validators import OnlyDiggitsValidator
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
            OnlyDiggitValidator() #Must contain only digits
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
    