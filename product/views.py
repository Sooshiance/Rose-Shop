from django.shortcuts import render
from rest_framework.response import Response

from .models import Category, Brand, Product, Rate
from .serializers import RateSerializer
