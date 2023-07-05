from django.contrib import admin
from product.models import Category

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Category, CategoryAdmin)