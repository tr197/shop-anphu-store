from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')


def show_category(request):
    return render(request, 'product/page_category.html')