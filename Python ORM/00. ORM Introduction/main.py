# models.py

from django.db import models

# Create your models here.
class BaseCharacter(models.Model):
    class Meta:
        abstract = True
        
    name = models.CharField(
        max_length=100,
    )
    
    description = models.TextField()
    
    
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
    
    
class TimeMage(Mage):
    time_magic_mastery = models.CharField(
        max_length=100,
    ) 
    
    temporal_shift_ability = models.CharField(
        max_length=100,
    )  
    
    
class Necromancer(Mage):
    raise_dead_ability = models.CharField(
        max_length=100,
    )  
    
    
class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(
        max_length=100,
    )  
        
    venomous_bite_ability = models.CharField(
        max_length=100,
    ) 
    
    
class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(
        max_length=100,
    ) 


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(
        max_length=100,
    ) 
    
    retribution_ability = models.CharField(
        max_length=100,
    ) 


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(
        max_length=100,
    )      
    
    
# caller.py

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Mage, Necromancer


# Create queries within functions

mage = Mage.objects.create(
    name="Fire Mage",
    description="A powerful mage specializing in fire magic.",
    elemental_power="Fire",
    spellbook_type="Ancient Grimoire"
)

necromancer = Necromancer.objects.create(
    name="Dark Necromancer",
    description="A mage specializing in dark necromancy.",
    elemental_power="Darkness", spellbook_type="Necronomicon",
    raise_dead_ability="Raise Undead Army"
)
print(mage.elemental_power)
print(mage.spellbook_type)
print(necromancer.name)
print(necromancer.description)
print(necromancer.raise_dead_ability)    