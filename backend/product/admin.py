from django.contrib import admin

from .models import Category, Feature, Product, Gallery, Color

from django_jalali.admin.filters import JDateFieldListFilter


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Feature, FeatureAdmin)


class GalleryAdmin(admin.TabularInline):
    model = Gallery


class ColorAdmin(admin.TabularInline):
    model = Color


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'category', 'is_active')
    list_filter = ['is_active',]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['vendor', 'title', 'category__title', 'feature__title']
    inlines = [GalleryAdmin, ColorAdmin]

admin.site.register(Product, ProductAdmin)
