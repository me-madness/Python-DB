from django.core.validators import MinLengthValidator, MaxLengthValidator
from main_app.validators import validate_menu_categories
from django.db import models
# from django.core.exceptions import ValidationError

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message="Name must be at least 2 characters long."),
            MaxLengthValidator(100, message="Name cannot exceed 100 characters." )
        ] 
    )
    
    location = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, message="Location must be at least 2 characters long."),
            MaxLengthValidator(200, message="Location cannot exceed 200 characters.")
        ]
    )
    
    description = models.TextField(null=True, blank=True)
    
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinLengthValidator(0, message="Rating must be at least 0.00."),
            MaxLengthValidator(5,"Rating cannot exceed 5.00.")
        ]
    )
    
    
class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )    
    
    description = models.TextField(
        validators=[validate_menu_categories]
    )
    
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE
    )