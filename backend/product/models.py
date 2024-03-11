from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.core.validators import MinValueValidator

from vendor.models import Vendor


User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title  = models.CharField(max_length = 50, unique=True, primary_key=True)
    description = models.CharField(max_length = 250)
    slug  = models.SlugField(max_length = 50, allow_unicode=True)
    pic  = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title


class Feature(models.Model):
    title  = models.CharField(max_length=50, unique=True, primary_key=True)
    description  = models.CharField(max_length=250)

    def __str__(self):
        return self.title        


class Product(models.Model):
    title       = models.CharField(max_length = 50, unique=True, primary_key=True)    
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    feature     = models.ManyToManyField(Feature)    
    description = models.CharField(max_length = 250)
    slug        = models.SlugField(max_length = 50, unique=True, allow_unicode=True)    
    pic         = models.ImageField(upload_to='product/')
    in_stock    = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price       = models.DecimalField(max_digits=12, decimal_places=0)
    shipping    = models.DecimalField(max_digits=6, decimal_places=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)
    vendor      = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} {self.category} {self.feature} {self.is_active}'
    
    def save(self, *args, **kwargs):
        super(Product, self).save()
        self.slug = slugify(self.title)

    def gallery(self):
        return Gallery.objects.filter(product=self)
    
    def color(self):
        return Color.objects.filter(product=self)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'All Product'


class Gallery(models.Model):
    photo_angle = models.CharField(max_length=30, blank=True, null=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    pic         = models.ImageField(upload_to='gallery/')
    active      = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.product}'


class Color(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    color_name = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product}'


# class Rate(models.Model):
#     product  = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user     = models.ForeignKey(User, on_delete=models.CASCADE)
#     vote     = models.CharField(max_length = 250, blank=True, null=True)    
#     rating   = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
#     average  = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(7)])

#     def __str__(self):
#         return f'{self.product} {self.user}'


# class Complaince(models.Model):
#     user           = models.ForeignKey(User, on_delete=models.CASCADE)
#     product        = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title          = models.CharField(max_length=30)
#     description    = models.CharField(max_length=250)
#     admin_approval = models.BooleanField(default=True)
#     created_at     = jmodels.jDateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.product} {self.user} {self.title} {self.admin_approval}'
