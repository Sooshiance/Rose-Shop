from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django_jalali.db import models as jmodels


class Category(models.Model):
    title       = models.CharField(max_length=256, verbose_name='نام', unique=True)
    cslug       = models.SlugField(allow_unicode=True, verbose_name='اسلاگ', unique=True,  primary_key=True)
    description = models.CharField(max_length=4096, verbose_name='توضیحات')
    pic         = models.ImageField(upload_to='category/', verbose_name='تصویر', default='')
    created_at  = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    
    def __str__(self) -> str:
        return f"{self.title}"


class Brand(models.Model):
    title       = models.CharField(max_length=256, verbose_name='نام', unique=True)
    bslug       = models.SlugField(allow_unicode=True, primary_key=True, unique=True, verbose_name='اسلاگ')
    country     = models.CharField(max_length=30, verbose_name='ساخت کشور')
    logo        = models.ImageField(upload_to='brand', verbose_name='لوگو', default='')
    description = models.CharField(max_length=2048, verbose_name='توضیحات')
    created_at  = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    
    def __str__(self) -> str:
        return f"{self.title} {self.country}"


class Product(models.Model):
    title         = models.CharField(max_length=256, verbose_name='نام', unique=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='از دسته')
    brand         = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='از برند')
    pslug         = models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ', primary_key=True)
    description   = models.CharField(max_length=4096, verbose_name='توضیحات')
    pic           = models.ImageField(upload_to='product/', verbose_name='تصویر', default='')
    country       = models.CharField(max_length=30, verbose_name='ساخت کشور')
    serial_number = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='بار کد')
    price         = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت')
    weight        = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='وزن')
    expiration    = models.DateField(verbose_name='تاریخ انقضا', null=True, blank=True)
    available     = models.BooleanField(default=True, verbose_name='وضعیت انبار')
    
    def __str__(self) -> str:
        return f"{self.title} {self.category} {self.brand} {self.available}"
    
    class Meta:
        ordering = ['title']


class Rate(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    product        = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    score          = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='امتیاز')
    description    = models.CharField(max_length=4096, verbose_name='توضیحات', null=True, blank=True)
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    
    def __str__(self) -> str:
        return f"{self.product} {self.user} {self.score} {self.admin_approval} {self.pk}"
