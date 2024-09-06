from django.contrib import admin

from .models import Category, Cart, Product, CartItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'category', 'price', 'quantity']
    list_filter = ['category']
    search_fields =['name', 'description']
    list_editable = ['price', 'quantity']
    ordering = ['name']
    readonly_fields = ['id']

class CartItemAdmin(admin.ModelAdmin):
    list_display =['product', 'quantity', 'total']
    search_fields = ['product', 'name']
    readonly_fields = ['total']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount']
    search_fields = ['user']


admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)

# 



# Register your models here.
