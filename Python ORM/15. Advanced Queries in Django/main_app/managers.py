from django.db import models


# Task 01.Available Products
class ProductManager(models.Manager):
    def available_products(self):
        return self.filter(is_available=True)
    
    def available_products_in_category(self, category_name: str):
        return self.filter(is_available=True, category_name=category_name)
    
    
    # Task 02. Product Quantity Ordered
    def product_quantity_ordered():
        # return f"Quantity ordered of {product_name1}: {total_ordered_quantity1}"