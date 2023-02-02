from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('buy/', buy_cart, name='by-cart'),
    path('delete-cart/',  delete_cart, name='delete-cart'),
    path('add-to-cart/<str:slug>',  add_to_cart, name='add-to-cart'),
    path('reduce-quantity-cart/<str:slug>',  reduce_quantity_cart, name='reduce-quantity-cart'),
    path('delete-order-cart/<str:slug>',  delete_order, name='delete-order'),
    path('product/<str:slug>', detail, name='detail'),
]