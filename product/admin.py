from django.contrib import admin
from product.models import Category, SubCategory, Product, ProductImages

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)




# Register your models here.
class ProductImageInLine(admin.TabularInline):
    model = ProductImages
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    inlines = [ProductImageInLine, ]
    ordering= ['category', 'slug',]
    list_filter = ['category',]
    search_fields = ['slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)