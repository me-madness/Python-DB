import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery


# Create and check models
def show_highest_rated_art() -> str:
    pass

# Run and print your queries
