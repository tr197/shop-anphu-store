import contextlib
from django.shortcuts import render, get_object_or_404
from product.models import Category, SubCategory, Product
from app.constants import CmpInfo

def index(request):
    top_categories = Category.objects.all()[:3]
    context = {
        'CmpInfo': CmpInfo,
        'top_categories': top_categories,
    }
    return render(request, 'product/index.html', context)


def show_all_categories(request):
    all_categories = Category.objects.all()

    context = {
        'all_categories': all_categories,
        'list_categories': all_categories,
        'CmpInfo': CmpInfo,
    }
    return render(request, 'product/page_products.html', context)



def show_list_categories(request, slug, category_id):
    all_categories = Category.objects.all()

    category = None
    with contextlib.suppress(Exception):
        category = Category.objects.get(id=category_id)

    list_category = category.children.all()
    list_products = category.products.all()

    context = {
        'all_categories': all_categories,
        'list_categories': list_category,
        'list_products': list_products,
        'category': category,
        'curent_category_id': category.id,
        'CmpInfo': CmpInfo,
    }
    return render(request, 'product/page_products.html', context)


def show_list_products(request, slug, sub_slug, sub_category_id):
    all_categories = Category.objects.all()

    sub_category, list_products = None, None

    with contextlib.suppress(Exception):
        sub_category = SubCategory.objects.get(id=sub_category_id)
        list_products = sub_category.products.all()
        

    context = {
        'all_categories': all_categories,
        'list_products': list_products,
        'category': sub_category.parent_category,
        'sub_category': sub_category,
        'curent_category_id': sub_category.id,
        'CmpInfo': CmpInfo,
    }
    return render(request, 'product/page_products.html', context)



def show_product_detail(request, category_slug, product_slug, product_id):

    product = get_object_or_404(Product, id=product_id)
    category = product.category
    curent_category_id = category.id

    all_categories = Category.objects.all()
    sub_category = None

    with contextlib.suppress(Exception):
        sub_category = SubCategory.objects.get(id=category.id)
        category = sub_category.parent_category

    context = {
        'all_categories': all_categories,
        'category': category,
        'sub_category': sub_category,
        'product': product,
        'other_images': product.other_images.all(),
        'curent_category_id': curent_category_id,
        'CmpInfo': CmpInfo,
    }

    return render(request, 'product/product_detail.html', context)