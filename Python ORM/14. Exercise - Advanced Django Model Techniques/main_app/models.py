from django.db import models
# from django.core.validators import EmailValidator
from main_app.validators import validate_name
from django.core.exceptions import ValidationError
# Create your models here.


# Task 01. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validate_name,
            (message="Name can only contain letters and spaces")
        ]
    )
    
    age = models.PositiveIntegerField(
        validators=[
            (message="Age must be greater than or equal to 18")
        ]
    )
    
    email = models.EmailField(
        validators=[
            EmailValidator(message="Enter a valid email address") 
        ]
    )
    
    phone_number = models.CharField(
        validators=[
            (message="Phone number must start with a '+359' followed by 9 digits")
        ]
    )
    
    website_url = models.URLField(
        validators=[
            (message="Enter a valid URL")
        ]
    )