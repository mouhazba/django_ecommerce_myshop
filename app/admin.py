from django.contrib import admin

from .models import Product, Order, Cart


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'name', 'price', 'stock', 'image', 'slug', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'quantity', 'ordered', 'ordered_date', 'product', 'user']


admin.site.register(Cart)
