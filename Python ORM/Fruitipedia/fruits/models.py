from django.db import models
from django.core.validators import MinLengthValidator
from validators import OnlyLettersValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )
    
    
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ]
    )    
    