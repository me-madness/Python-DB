from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
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
    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]
        
    title = models.CharField(
        max_length=100,
    )    
    
    description = models.TextField()
    
    genre = models.CharField(
        max_length=50,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    
class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"
        
    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, message="Author must be at least 5 characters long"),
        ]
    )  
    
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(6, message="ISBN must be at least 6 characters long"),
        ]
    )  
    
    
class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Model ofm type - Movie"
        
    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Director must be at least 8 characters long"),
        ]
    ) 
    
    
class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Model ofm type - Music"
        
    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, message="Artist must be at least 9 characters long"),
        ]
    ) 
    
    
# Task 03.Tax-Inclusive Pricing  
class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    
    
class DiscountProduct(Product):
    class Meta:
        proxy = True    
  
  
  
# Task 04.Superhero Universe



# Task 05.*Vector Searching         