from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
