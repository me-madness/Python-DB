import os
import django
from django.db.models import Q, Count
from main_app.models import Product

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Profile, Order



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
    ).order_by('full_name')
    
    if not profiles.exists():
        return ""
    
    return '\n'.join(
        f"Profile: {p.full_name}, email: {p.email}, phone_number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles       
    )
       
# print(get_profiles("ra"))    

def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()
    
    if not profiles.exists():
        return ""
    
    return "\n".join(
        f"Profile: {p.full_name}, orders: {p.orders.count()}"
        for p in profiles
    )
    
# print(get_loyal_profiles())    

def get_last_sold_products() -> str:
    last_order = Order.objects.prefetch_related('products').last()
    
    if last_order is None or not last_order.products.exists():
        return ""
    
    # First Option
    # products = ', '.join([p.name for p in last_order.products.order_by('name')]) 
    
    # Second Option
    products = ', '.join(last_order.products.order_by('name').values_list('name', flat=True))
    
    return f"last sold products: {products}"

# print(get_last_sold_products())


def get_top_products() -> str:
    top_products = Product.objects.annotate(
        orders_count=Count('orders')
    ).filter(
        orders_count__gt=0,
    ).order_by(
        '-order_count',
        'name'
    )[:5]
    
    if