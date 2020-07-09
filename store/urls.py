from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.index, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('cart/add_one/<int:product_id>', views.add_one_to_cart, name='add_one_to_cart'),
    path('cart/remove/<int:product_id>', views.remove_one_from_cart, name='remove_one_from_cart'),
]