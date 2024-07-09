from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        
    #  "Name must be at least 2 characters long."   
    #  "Name cannot exceed 100 characters."   
    )
    
    location = models.CharField(
        max_length=200,
        
    # "Location must be at least 2 characters long."    
    # "Location cannot exceed 200 characters."
    )
    
    description = models.TextField()
    
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        
        # "Rating must be at least 0.00."
        # "Rating cannot exceed 5.00."
    )