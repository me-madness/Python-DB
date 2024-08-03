from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Astounaut(models.Model):
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
            #Must contain only digits
        ]
    )
    
    is_active = models.BooleanField(
        default=True,
    )
    
    