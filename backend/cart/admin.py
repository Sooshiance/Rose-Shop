from django.contrib import admin

from .models import Cart, CartOrder, CartOrderItem, Copoun, Wishlist


class CartAdmin(admin.ModelAdmin):
    list_display = ('product',)

admin.site.register(Cart, CartAdmin)


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('vendor',)

admin.site.register(CartOrder, CartOrderAdmin)


class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product')

admin.site.register(CartOrderItem, CartOrderItemAdmin)


class CopounAdmin(admin.ModelAdmin):
    list_display = ('vendor',)

admin.site.register(Copoun, CopounAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('product',)

admin.site.register(Wishlist, WishlistAdmin)
