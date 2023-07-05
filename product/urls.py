from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('dong-san-pham/', views.show_category, name='category'),
]

