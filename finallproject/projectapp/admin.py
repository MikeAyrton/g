from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'color')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(SendMessage)





