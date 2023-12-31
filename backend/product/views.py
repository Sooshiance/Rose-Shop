from rest_framework.response import Response
from rest_framework import generics, permissions

from .models import Category, Brand, Product, Rate
from .serializers import *


class CategoryAPIView(generics.ListAPIView):
    """
    All Categories in here
    """
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    See each Category seprately
    """
    def get(self, request, cslug):
        category = Category.objects.get(cslug=cslug)
        serialize = CategorySerializer(category)
        return Response(serialize.data)


class BrandAPIView(generics.ListAPIView):
    """
    See all Brand in one
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]


class ProductAPIView(generics.ListAPIView):
    """
    See all products in one
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    See each product individually
    """
    def get(self, request, pslug):
        product = Product.objects.get(pslug=pslug)
        serialize = ProductSerializer(product)
        return Response(serialize.data)


class ProductRateAPIView(generics.CreateAPIView):
    """
    Users send their comments
    """
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
