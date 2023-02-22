from xml.etree.ElementInclude import include
from django.urls import path
from . import views
urlpatterns = [
    path('',views.product,name="home"),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.user_login,name="signin"),
    path('logout/',views.user_logout,name="logout"),
    path('product_details/<int:id>/',views.product_details,name="product_details"),
    path('product_details/',views.product_details,name="product_details"),
    path('add_to_cart/<int:id>/',views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_view, name='cart'),
    path('remove_from_cart/<int:id>/',views.remove_from_cart, name='remove_from_cart'),
    path('place_order/',views.place_order,name="place_order"),
]
