from decimal import Decimal
from django.db import models
from django.db.models import QuerySet


# Task 01.Real Estate Listing
class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)
    
    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__range=[min_price, max_price])
    
    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter()