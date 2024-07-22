from django.db import models
from django.core.validators import MinLengthValidator


class DateTime(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True
    )

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2)
        ]
    )
    
    email = models.EmailField()
    
    phone_number = models.CharField(
        max_length=15,
    )
    
    address = models.TextField()
    
    is_active = models.BooleanField(
        default=False,
    )
    