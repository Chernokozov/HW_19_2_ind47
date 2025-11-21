from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product,  Category
from .forms import ProductForm


def home(request):
    """Контроллер для главной страницы с пагинацией"""
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products_list, 4)  # 4 товара на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_create(request):
    """Создание нового продукта"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {'form': form})


def product_update(request, pk):
    """Редактирование продукта"""
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/product_form.html', {'form': form})


def product_delete(request, pk):
    """Удаление продукта"""
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('home')

    return render(request, 'catalog/product_confirm_delete.html', {'product': product})

def media_test(reequest):
    """Страница для тестирования медифайлов"""
    return render(request, 'catalog/media_test.html')