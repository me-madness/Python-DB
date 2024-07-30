import os
import django
from decimal import Decimal
from django.db.models import Q, Count, F, Case, When
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
        '-orders_count',
        'name'
    )[:5]
    
    if not top_products.exists():
        return ""
    
    product_lines = "\n".join(f"{p.name}, sold {p.orders_count} times" for p in top_products)
    return f"Top products:\n" + product_lines


def apply_discounts() -> str:
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    ).update(
        total_prise=F('total_price') * Decimal(0.90)
    )

    return f"Discount applied to {updated_orders_count} orders"


def complete_order() -> str:
    order = Order.objects.filter(
        is_completed=False
    ).order_by(
        'creation_date'
    ).first()
    
    if not order:
        return ""
    
    for product in order.products.all():
        product.in_stock -= 1
        
        if product.in_stock == 0:
            product.is_available = False
            
        product.save()
        
    Product.objects.filter(order=order).update(
        in_stock=F('in_stock') -1,
        is_available=Case(
            When(in_stock=1)
        )
    )    
            