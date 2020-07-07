from django.shortcuts import render, get_object_or_404
from .models import Product, Category

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

def cart(request):
    return render(request, 'store/cart.html')
