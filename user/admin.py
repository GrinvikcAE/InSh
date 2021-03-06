from django.contrib import admin
from .models import *

class UserAdmin (admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    class Meta:
        model = User


admin.site.register(User, UserAdmin)
