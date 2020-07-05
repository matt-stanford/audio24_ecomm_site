from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html', {})

def product(request):
    return render(request, 'store/product.html', {})
