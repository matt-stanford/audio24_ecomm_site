from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

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
    except Exception as e:
        raise e
    return render(request, 'store/product.html', {'product': product})

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

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'store/cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')