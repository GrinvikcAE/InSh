from django.contrib import admin
from .models import *


class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_filter = ['name', 'from_company']
    search_fields = ['name', 'from_company']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
