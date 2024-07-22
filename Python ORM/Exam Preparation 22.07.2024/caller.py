import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Profile


# Create queries within functions
def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""
    
    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
            |
        Q(email__icontains=search_string)
            |
        Q(phone_number__icontains=search_string)
    )
    
    if not profiles.exists():
        return ""
    
    return '\n'.join(
        f"Profile: {p.full_name}, email: {p.email}, phone_number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles       
    )
    
    
print(get_profiles("ra"))    