from django.db import models

class Shoe(models.Model):
    brand = models.CharField(
       max_length=25, 
    )

    size = models.PositiveBigIntegerField()
    

class UniqueBrands(models.Model):
        brand = models.CharField(
            max_length=25,
            unique=True,
        )
        
        
class EventRegistration(models.Model):
    event_name = models.CharField(
        max_length=50,
    )

    participant_name = models.CharField(
        max_length=60,
    )

    registration_date = models.DateField()

    def __str__(self):
        return f"{self.participant_name} - {self.event_name}"        