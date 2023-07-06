import contextlib
from django.shortcuts import render
from product.models import Category, SubCategory, Product

def index(request):
    return render(request, 'product/index.html')


def show_all_categories(request):
    all_categories = Category.objects.all()

    context = {
        'all_categories': all_categories,
        'list_categories': all_categories,
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
        'category': category
    }
    return render(request, 'product/page_products.html', context)


def show_list_products(request, slug, sub_slug, sub_category_id):
    all_categories = Category.objects.all()

    sub_category, list_products = None, None
    sub_category = None
    with contextlib.suppress(Exception):
        sub_category = SubCategory.objects.get(id=sub_category_id)
        list_products = sub_category.products.all()
        

    context = {
        'all_categories': all_categories,
        'list_products': list_products,
        'category': sub_category.parent_category,
        'sub_category': sub_category
    }
    return render(request, 'product/page_products.html', context)

# show_list_products