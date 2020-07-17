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
    path('thankyou/<int:order_id>', views.thanks_page, name='thanks_page'),
    path('account/signup/', views.signupView, name='signup'),
    path('account/signin/', views.signinView, name='signin'),
    path('account/signout/', views.signoutView, name='signout'),
    path('order_history/', views.orderHistory, name='order_history'),
    path('order/<int:order_id>', views.viewOrder, name='order_detail'),
    path('search/', views.search, name='search'),
    path('wishlist/add/<int:product_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlistView, name='wishlist'),
    path('wishlist/remove/<int:product_id>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('privacy/', views.price_match_privacy, name='price_match_privacy'),
    path('price-match-guarantee/', views.price_match_guarantee, name='price_match_guarantee'),
]