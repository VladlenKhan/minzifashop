from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('shop/',shop,name='shop'),
    path('products/<int:product_id>/',product_detail, name='product_detail'),
    path('categories/<int:category_id>/',category_detail, name='category_detail'),
]