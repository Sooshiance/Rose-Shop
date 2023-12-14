from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView

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
