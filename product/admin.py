from django.contrib import admin

from .models import Category, Brand, Product, Rate


@admin.register(Category)
class CAdmin(admin.ModelAdmin):
    list_display = ['title', 'cslug']
    prepopulated_fields = {'cslug':('title',)}


@admin.register(Brand)
class BAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']
    prepopulated_fields = {'bslug':('title',)}


@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'country', 'available']
    prepopulated_fields = {'pslug':('title',)}


@admin.register(Rate)
class PAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'score', 'admin_approval']
