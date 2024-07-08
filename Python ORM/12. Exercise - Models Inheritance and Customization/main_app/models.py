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
    

class UserProfile(models.Model):
    username = models.CharField(
        max_length=70,
        unique=True,
    )  
    
    email = models.EmailField(
        unique=True,
    )
    
    bio = models.TextField(
        null=True,
        blank=True,
    )
    
    
class Message(models.Model):
    sender = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    
    receiver = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name="receiver_messages",
    )    
    
    content = models.TextField()
    
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    
    is_read = models.BooleanField(
        default=False,
    )
    
    def mark_as_read(self) -> None:
        self.is_read = True
        # good to save it
        
    def reply_to_message(self, reply_content: str) -> "Message":
        message = Message(
            sender=self.receiver,
            receiver=self.sender,
            content=reply_content
        )
        
        message.save()
        
        return message
    
    
    def forward_message(receiver: UserProfile):
        pass    