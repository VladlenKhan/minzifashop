from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
  
    return render(request,'home.html',{'category':category,'product':product})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products.html', {'product': product})

def shop(request):
    product = Product.objects.all()
    return render(request, 'shop.html', {'product': product})