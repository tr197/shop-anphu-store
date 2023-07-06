from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('san-pham/', views.show_all_categories, name='category'),
    path('san-pham/<slug:slug>/<str:category_id>/', views.show_list_categories, name='list-category'),
    path('san-pham/<slug:slug>/<slug:sub_slug>/<str:sub_category_id>',
          views.show_list_products, name='list-products'),
]

