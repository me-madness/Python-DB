from django.db import models
from django.db.models import QuerySet


# Task 01.Real Estate Listing
class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str) -> QuerySet:
        