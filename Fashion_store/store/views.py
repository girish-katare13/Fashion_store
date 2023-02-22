
from django.shortcuts import render,redirect
from .models import Product,Cart,Order
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponse
import os

# Create your views here.
def product(request):
    item = Product.objects.all()
    return render(request,"home.html",{'item':item})

def signup(request):
    if request.method == 'POST':
        print("gvg")
        obj = CustomUserCreationForm(request.POST)
        if obj.is_valid():
            print("is")
            print(obj.cleaned_data['username'])
            obj.save()
        
    else:   
        obj = CustomUserCreationForm()        

    
    return render(request,'signup.html',{'form':obj})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request,data=request.POST)
        print("fukna")
        if form.is_valid():
            print("chokya")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("log in")
                return redirect('home')  
    else:
    
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def product_details(request,id=None):
    obj = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=obj.category).exclude(id=id)
    return render(request,'product_details.html',{"obj":obj, 'related_products': related_products})

def add_to_cart(request, id=None):
    print("hi all")
    obj = Product.objects.get(id=id)
    user = request.user
    name = obj.name
    price = obj.price
    size = obj.size
    img = obj.img 
    description = obj.description
    print(name)
    Cart(user=user,name=name,price=price,size=size,img=img,description=description).save()
    return redirect('cart')

def cart_view(request):
    obj = Cart.objects.filter(user = request.user)
    print(obj.count())
    if obj.count() < 1:
        print("njvnd")
        msg = "Me ahe to nalayak"
        return render(request, 'cart.html', {"msg" : msg})
    total = Cart.total_price_of_items(obj)
    return render(request, 'cart.html',{'obj':obj,'total':total})

def remove_from_cart(request,id = None):
    Cart.objects.filter(id = id).delete()
    return redirect("cart")

@login_required
def place_order(request):
    print("place block")
    if request.method == 'POST':
        print("working")
        # Get the current user's cart
        cart = Cart.objects.filter(user=request.user)
        print(cart)

        # Loop through each item in the cart and add it to the order
        for obj in cart:
            print("hiii")
            print(obj)
            name = obj.name  
            user = request.user
            total_price = obj.price
            Order.objects.create(user=user, name=name, total_price=total_price).save()

        # Clear the cart
        cart.delete()
        order = Order.objects.all()

        # Redirect to the order confirmation page
        return render(request, 'place_order.html', {'order': order})