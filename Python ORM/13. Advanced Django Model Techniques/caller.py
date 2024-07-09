import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Restaurant, Menu
from django.core.exceptions import ValidationError

# Create queries within functions

from main_app.models import Restaurant, Menu

# Keep the data from the previous exercise, so you can reuse it

