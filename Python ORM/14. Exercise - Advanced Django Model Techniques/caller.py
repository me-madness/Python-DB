import os
from decimal import Decimal
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer, Book, Product, DiscountedProduct, FlashHero, SpiderHero
from decimal import Decimal
from django.core.exceptions import ValidationError


# Create queries within functions

# Create a Product instance
