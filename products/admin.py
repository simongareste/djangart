from django.contrib import admin

# Register your models here.
from .models import Product, ProductsBundle

admin.site.register(Product)
admin.site.register(ProductsBundle)
