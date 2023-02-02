from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse


from .models import Product, Cart, Order


def home(request):
    images_popular = Product.objects.all()[:5]
    products = Product.objects.all()
    '''
    if request.user.is_authenticated:
        print("welcome", request.user)
    else:
        print(request.user)
        print(request.session)
    '''

    return render(request, 'app/home.html', context={'list_products': products, 'popular': images_popular})


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'app/detail.html', context={'detail_product': product})


def about(request):
    return render(request, 'app/about.html')


def cart(request):
    if request.user.is_authenticated:
        cart_user, _ = Cart.objects.get_or_create(user=request.user)
        orders = cart_user.orders.all()
        total = 0
        for i in orders:
            total += i.get_cart_cost
        context = {'orders': orders, 'total': total}
        return render(request, 'app/cart.html', context)
    else:
        return render(request, 'app/cart.html')


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart_user, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created:
        cart_user.orders.add(order)
        cart_user.save()
    else:
        if order.quantity < product.stock:
            order.quantity += 1
            order.save()

    return redirect('cart')


def checkout(request):
    if request.user.is_authenticated:
        cart_user, _ = Cart.objects.get_or_create(user=request.user)
        orders = cart_user.orders.all()
        total = 0
        for i in orders:
            total += i.get_cart_cost
        context = {'orders': orders, 'total': total}
        return render(request, 'app/checkout.html', context)
    else:
        return render(request, 'app/checkout.html')


def reduce_quantity_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart_orders = Order.objects.filter(user=user, ordered=False)
    order = get_object_or_404(Order, user=user, ordered=False, product=product)
    user_cart = Cart.objects.filter(user=user)

    total = 0
    for i in cart_orders:
        total += 1

    if total > 1:
        print("total >1", total)
        if order.quantity >= 1:
            order.quantity -= 1
            order.save()

        if order.quantity == 0:
            total -= 1
            order.delete()

    if total == 1:
        print("total = 1", total)
        if order.quantity >= 1:
            order.quantity -= 1
            order.save()

        if order.quantity == 0:
            total -= 1
            order.delete()
            user_cart.delete()
    return redirect('cart')


def delete_cart(request):
    user = request.user
    orders = Order.objects.filter(user=user, ordered=False)
    carts = get_object_or_404(Cart, user=user)
    if user:
        orders.delete()
        carts.delete()
    return redirect('cart')


def delete_order(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart_orders = Order.objects.filter(user=user, ordered=False)
    order = get_object_or_404(Order, user=user, ordered=False, product=product)
    user_cart = Cart.objects.filter(user=user)

    total = 0
    for i in cart_orders:
        total += 1

    if total > 1:
        order.delete()
    else:
        order.delete()
        user_cart.delete()
    return redirect('cart')


def buy_cart(request):
    pass


















"""
    #return redirect(reverse("detail", kwargs={'slug': slug}))

def delete_cart_bis(request):
    cart_user = request.user.cart
    if cart_user:
        cart_user.delete()

    return redirect('home')
    
    
def buy_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    carts, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created:
        carts.orders.add(order)
        carts.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("detail", kwargs={'slug': slug}))

"""



