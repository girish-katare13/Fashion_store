from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    isproduct_active = models.BooleanField()

    def __str__(self) :
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=122)
    price = models.FloatField(default=0.00)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='media/')

    
    def __str__(self) :
        return self.name
    @staticmethod
    def total_price_of_items(data):
        total=0
        for product in data:
            total += product.quantity * product.price

        return total


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    name = models.CharField(max_length=122)
