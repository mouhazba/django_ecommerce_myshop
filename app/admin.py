from django.contrib import admin

from .models import Product, Order, Card


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'name', 'price', 'stock', 'image', 'slug', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'quantity', 'ordered', 'ordered_date', ]


admin.site.register(Card)