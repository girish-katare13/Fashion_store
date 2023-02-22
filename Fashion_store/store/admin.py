from django.contrib import admin

from .models import Product,Cart,Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_displays = ("name","price","quantity")

class CartAdmin(admin.ModelAdmin):
    list_displays = ("name","price")

class OrderAdmin(admin.ModelAdmin):
    list_displays = ("order_date")

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)

