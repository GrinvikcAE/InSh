from django.contrib import admin
from .models import *

class StateAdmin (admin.ModelAdmin):
    list_display = [field.name for field in State._meta.fields]
    fields = []

    class Meta:
        model = State

class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    fields = []

    class Meta:
        model = Order

class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    fields = []

    class Meta:
        model = ProductInOrder

class ProductInCanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCan._meta.fields]

    class Meta:
        model = ProductInCan


admin.site.register(State, StateAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInCan, ProductInCanAdmin)


