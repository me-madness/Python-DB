# Generated by Django 5.0.6 on 2024-07-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_discountproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DiscountProduct',
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]
