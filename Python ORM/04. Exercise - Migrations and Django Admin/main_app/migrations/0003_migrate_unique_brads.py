# Generated by Django 5.0.4 on 2024-06-24 17:06

from django.db import migrations


# Is not right to add like that
# from main_app.models import Shoe


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')
    
    unique_brands_name = shoe.objects.values_list('brand', flat=True).distinct()

    # Right Way
    unique_brands.objects.bulk_create([unique_brands(brand_name=brand_name) for brand_name in unique_brands_name])

    # Wrong Way
    # for brand_name in unique_brands_name:
    #     unique_brands.create(brand_name=brand_name) # INSERT INTO unique_brands(brand_name) VALUES (brand_name)

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
    ]
