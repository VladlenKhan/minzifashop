from django.shortcuts import render
from .models import *
def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    return render(request,'home.html',{'category':category,'product':product})

def shop(request):
    return render(request,'shop.html')