from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, RegexValidator


class DateTime(models.Model):
    class Meta:
        abstract = True
        
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )    
        
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

class Astronaut(DateTime):
    # name = models.CharField(
    #     max_length=120,
    #     validators=[
    #         MinLengthValidator(2)
    #     ]
    # )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d+$', message='Phone number must contain only digits.')
        ]
    )
    is_active = models.BooleanField(
        default=True,
    )
    
    date_of_birth = models.DateField(
        null=True, 
        blank=True,
    )
    
    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    # updated_at = models.DateTimeField(
    #     auto_now=True,
    # )

    # def __str__(self):
    #     return self.name

class Spacecraft(DateTime):
    # name = models.CharField(
    #     max_length=120,
    #     validators=[
    #         MinLengthValidator(2)
    #     ]
    # )
    
    manufacturer = models.CharField(
        max_length=100
    )
    
    capacity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    
    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )
    launch_date = models.DateField()
    
    # updated_at = models.DateTimeField(
    #     auto_now=True,
    # )

    # def __str__(self):
    #     return self.name

class Mission(DateTime):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ]

    # name = models.CharField(
    #     max_length=120,
    #     validators=[
    #         MinLengthValidator(2)
    #     ]
    # )
    description = models.TextField(
        null=True,
        blank=True,
    )
    
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='Planned'
    )
    
    launch_date = models.DateField()
    
    # updated_at = models.DateTimeField(
    #     auto_now=True,
    # )
    
    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
    )
    
    astronauts = models.ManyToManyField(
        to=Astronaut,
    )
    
    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        related_name='missions_as_commander'
    )

    # def __str__(self):
    #     return self.name







# from django.db import models
# from django.core.validators import MinLengthValidator,MinValueValidator, RegexValidator 
# from validators import OnlyDigitsValidator
# # Create your models here.


# class DateTime(models.Model):
#     class Meta:
#         abstract = True
        
#     name = models.CharField(
#         max_length=120,
#         validators=[
#             MinLengthValidator(2)
#         ]
#     )    
        
#     updated_at = models.DateTimeField(
#         auto_now_add=True,
#     )
   

# class Astronaut(DateTime):
    
#     phone_number = models.CharField(
#         max_length=15,
#         unique=True,
#         validators=[
#             # RegexValidator(regex=r'^\d+$', message='Phone number must contain only digits.')
#             OnlyDigitsValidator()
#         ]
#     )
    
#     is_active = models.BooleanField(
#         default=True,
#     )
    
#     date_of_birth = models.DateField(
#         null=True,
#         blank=True,
#     )
    
#     spacewalks = models.IntegerField(
#         default=0,
#         validators=[
#             MinValueValidator(0)
#         ]
#     )
    
   
# class Spacecraft(DateTime):   
    
#     manufacturer = models.CharField(
#         max_length=100,
#     )
    
#     capacity = models.PositiveSmallIntegerField(
#         validators=[
#             MinValueValidator(1)
#         ]
#     )
    
#     weight = models.FloatField(
#         validators=[
#             MinValueValidator(0.0)
#         ]
#     )
    
#     launch_date = models.DateField()
    

# class Mission(DateTime):
    
#     STATUS_CHOICES = [
#         ('Planned', 'Planned'),
#         ('Ongoing', 'Ongoing'),
#         ('Completed', 'Completed')
#     ]
    
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
    
#     status = models.CharField(
#         max_length=9,
#         choices=STATUS_CHOICES,
#         default="Planned",
#     )
    
#     launch_date = models.DateField()
    
#     spacecraft = models.ForeignKey(
#         to=Spacecraft,
#         on_delete=models.CASCADE,
#     )
    
#     astronauts = models.ManyToManyField(Astronaut)
    
#     commander = models.ForeignKey(
#         to=Astronaut,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="missions_as_commander"
#     )