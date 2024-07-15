from decimal import Decimal
from django.db import models
from django.db.models import QuerySet, Count, Max


# Task 01.Real Estate Listing
class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)
    
    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__range=[min_price, max_price])
    
    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter(bedrooms=bedrooms_count)
    
    def popular_locations(self) -> QuerySet:
        return self.values('location').annotate(
            location_count=Count('location')
        ).order_by('-location_count', 'location')[:2]
        
        
# Task 02.Video Games Library        
class VideoGameManager(models.Manager):
    
    def games_by_genre(self, genre: str) -> QuerySet:
        return self.filter(genre=genre)
    
    def recently_released_games(self, year: int) -> QuerySet:
        return self.filter(year__gte=year)
    
    def highest_rated_game(self) -> QuerySet:
        # First option with aggregate
        # max_rating = self.aggregate(max_rating=Max('rating'))['max_rating']
        # game_with_max_rating = self.filter(rating=max_rating)
        
        # Second option with annotate
        return self.annotate(max_rating=Max('rating')).order_by('-max_rating').first()
    
    def lowest_rated_game(self) -> QuerySet:
        pass
    
    def average_rating(self) -> QuerySet:
        pass  