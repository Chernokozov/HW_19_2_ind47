from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    lastest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 товаров: ")
    for product in lastest_products:
        print(f'- {product.name}: {product.price} руб. (Категория: {product.category.name})')
    return render(request, "home.html", {'latest_products':lastest_products})


def contacts(request):
    return render(request, "contacts.html")
