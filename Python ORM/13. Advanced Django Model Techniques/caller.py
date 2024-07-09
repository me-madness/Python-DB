import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


# Create queries within functions

from main_app.models import Restaurant, RegularRestaurantReview, FoodCriticRestaurantReview
from django.core.exceptions import ValidationError

restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
