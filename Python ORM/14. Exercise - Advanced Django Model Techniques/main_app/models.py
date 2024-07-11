from django.db import models
from django.core.validators import MinValueValidator, EmailValidator
from main_app.validators import ValidateName
from django.core.exceptions import ValidationError
# Create your models here.


# Task 01. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            ValidateName("Name can only contain letters and spaces")
        ]
    )
    
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18, message="Age must be greater than or equal to 18"),
        ]
    )
    
    email = models.EmailField(
        error_messages={'Invalid': "Enter a valid email address"}
    )
    
    phone_number = models.CharField(
        validators=[
            ("Phone number must start with a '+359' followed by 9 digits")
        ]
    )
    
    website_url = models.URLField(
        validators=[
            ("Enter a valid URL")
        ]
    )