from django.contrib import admin
from product.models import Category, SubCategory, Product

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, ProductAdmin)
admin.site.register(SubCategory, ProductAdmin)
admin.site.register(Product, ProductAdmin)