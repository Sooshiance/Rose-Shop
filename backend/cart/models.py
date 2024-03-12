from django.db import models
from django.conf import settings

from .enums import PaymentStatus, OrderStatus

from product.models import Product
from vendor.models import Vendor

from django_jalali.db import models as jmodels


User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    quantitty  = models.PositiveIntegerField(default=1)
    price      = models.DecimalField(max_digits=12, decimal_places=0)
    subtotal   = models.DecimalField(max_digits=12, decimal_places=0)
    shipping   = models.DecimalField(max_digits=12, decimal_places=0)
    tax_fee    = models.DecimalField(max_digits=12, decimal_places=0)
    total      = models.DecimalField(max_digits=12, decimal_places=0)
    color      = models.CharField(max_length = 30)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.product}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "User Cart"


class CartOrder(models.Model):
    vendor         = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    buyer          = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subtotal       = models.DecimalField(max_digits=12, decimal_places=0)
    shipping       = models.DecimalField(max_digits=12, decimal_places=0)
    tax_fee        = models.DecimalField(max_digits=12, decimal_places=0)
    total          = models.DecimalField(max_digits=12, decimal_places=0)

    payment_status = models.CharField(max_length=50, choices=PaymentStatus.Paymant_Status, default="pending")
    order_staus    = models.CharField(max_length=50, choices=OrderStatus.Order_STATUS, default="Pending")

    # Copoun
    initial_total  = models.DecimalField(max_digits=12, decimal_places=0)
    saved_total    = models.DecimalField(max_digits=12, decimal_places=0)    

    created_at     = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vendor} {self.buyer}'    
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "User Cart Order User"


class CartOrderItem(models.Model):
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    order         = models.ForeignKey(CartOrder, on_delete=models.CASCADE)

    subtotal      = models.DecimalField(max_digits=12, decimal_places=0)
    shipping      = models.DecimalField(max_digits=12, decimal_places=0)
    tax_fee       = models.DecimalField(max_digits=12, decimal_places=0)
    total         = models.DecimalField(max_digits=12, decimal_places=0)

    # Copoun
    initial_total = models.DecimalField(max_digits=12, decimal_places=0)
    saved_total   = models.DecimalField(max_digits=12, decimal_places=0)

    created_at    = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} {self.order}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "User Cart Item Order"


class Copoun(models.Model):
    vendor     = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    user_by    = models.ManyToManyField(User, blank=True)
    code       = models.CharField(max_length = 256)
    discount   = models.IntegerField(default=1)
    active     = models.BooleanField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vendor} {self.user_by}'


class Wishlist(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField(default=1)
    color      = models.CharField(max_length = 30)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} {self.user}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "User Wish List"