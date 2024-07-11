from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from main_app.validators import ValidateName, validate_name
from django.core.exceptions import ValidationError
# Create your models here.


# Task 01. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validate_name,
            # ValidateName("Name can only contain letters and spaces")
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
        max_length=13,
        validators=[
            RegexValidator(regex=r'^\+359\d{9}$', 
                           message="Phone number must start with a '+359' followed by 9 digits")
        ]
    )
    
    website_url = models.URLField(
        error_messages={'invalid': 'Enter a valid URL'}
    )
    
    
# Task 02.Media
class BaseMedia(models.Model):
    title = models.CharField(
        max_length=100
    )    
    
    description = models.TextField()
    
    genre = models.CharField(
        max_length=50
    )
    
    created_at = models.DateTimeField()
    
    
class Book(models.Model):
    author = models.CharField(
        max_length=100,
        validators=[
            MinValueValidator(5, message="Author must be at least 5 characters long")
        ]
    )  
    
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinValueValidator(6, message="ISBN must be at least 6 characters long")
        ]
    )  
    
    
class Movie(models.Model):
    director = models.CharField(
        max_length=100,
        validators=[
            MinValueValidator(8, message="Director must be at least 8 characters long")
        ]
    ) 
    
    
class Music(models.Model):
    artist = models.CharField(
        max_length=100,
        validators=[
            MinValueValidator(9, message="Artist must be at least 9 characters long")
        ]
    ) 
    
    
            