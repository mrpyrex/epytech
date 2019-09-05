from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.


def category(request, c_slug=None):
    c_page = None
    products = None
    categories = Category.objects.all()

    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    context = {
        'category': c_page,
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/category.html', context)


def shop(request):
    products = Product.objects.all()
    context = {
        'title': 'Shop',
        'products': products
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'title': 'Shop',
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)


def category_detail(request, c_slug):
    category = get_object_or_404(Category, slug=c_slug)
    context = {
        'category': category
    }

    return render(request, 'shop/category_detail.html', context)
