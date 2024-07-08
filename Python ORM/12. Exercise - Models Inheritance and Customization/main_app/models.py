from django.db import models

# Create your models here.
class BaseCharacter(models.Model):
    class Meta:
        abstract = True
        
    name = models.CharField(
        max_length=100,
    )
    
    description = models.TextField
    
    
class Mage(BaseCharacter):
    elemental_power = models.CharField(
        max_length=100,
    )    
    
    spellbook_type = models.CharField(
        max_length=100,
    )
    
    
class Assassin(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100,
    )    
    
    assassination_technique  = models.CharField(
        max_length=100,
    ) 
    
    
class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100,
    )    
    
    demon_slaying_ability = models.CharField(
        max_length=100,
    )
    
    
    