from rest_framework.serializers import ModelSerializer

from .models import Category, Brand, Product, Rate


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'cslug', 'description', 'pic']


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'bslug', 'logo', 'country', 'description']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'pslug', 'pic', 'weight', 'expiration',
                  'country', 'description', 'serial_number', 'price', 'available']


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate 
        fields = ['score', 'description']
