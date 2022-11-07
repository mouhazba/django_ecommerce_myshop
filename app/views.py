from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'app/home.html', context={'list_products': products})


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'app/detail.html', context={'detail_product': product})


def about(request):
    return render(request, 'app/about.html')


