from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import stripe
from django.conf import settings

def index(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    context = {
        'category': category_page,
        'products': products
    }

    return render(request, 'store/index.html', context)

def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        price = float(product.price)

        three_monthly = round(price / 3, 2)

        six_apr = 0.0085333333
        six_monthly = round(price * ((six_apr * ((1+six_apr) ** 6)) / ((1+six_apr) ** 6 - 1)), 2)
        six_total = round(six_monthly * 6, 2)
        six_interest = round(six_total - price, 2)

        twelve_apr = 0.0084833333
        twelve_monthly = round(price * ((twelve_apr * ((1+twelve_apr) ** 12)) / ((1+twelve_apr) ** 12 - 1)), 2)
        twelve_total = round(twelve_monthly * 12, 2)
        twelve_interest = round(twelve_total - price, 2)

    except Exception as e:
        raise e
    context = {
        'product': product,
        'three_monthly': three_monthly,
        'six_monthly': six_monthly,
        'six_total': six_total,
        'six_interest': six_interest,
        'twelve_monthly': twelve_monthly,
        'twelve_total': twelve_total,
        'twelve_interest': twelve_interest
    }

    return render(request, 'store/product.html', context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST['quantity'])
        if quantity > 0:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
            except Cart.DoesNotExist:
                cart = Cart.objects.create(cart_id=_cart_id(request))
                cart.save()
            try:
                cart_item = CartItem.objects.get(product=product, cart=cart)
                if cart_item.quantity + quantity < cart_item.product.stock:
                    cart_item.quantity += quantity
                cart_item.save()
            except CartItem.DoesNotExist:
                cart_item = CartItem.objects.create(
                            product = product,
                            quantity = quantity,
                            cart = cart
                    )
                cart_item.save()

            return redirect('cart_detail')
        return HttpResponse(status=204)

def add_one_to_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')

def remove_one_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'audio24 - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='usd',
                description=description,
                customer=customer.id
            )
        except stripe.error.CardError as e:
            return False, e

    return render(request, 'store/cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total, description=description))

def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')