from django.contrib import admin
from .models import *


class CompanyAdmin (admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)
