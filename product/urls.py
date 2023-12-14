from django.urls import path 

from .views import *


urlpatterns = [
    path('', CategoryAPIView.as_view(), name='all-category'),
    path('<str:cslug>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products', ProductAPIView.as_view(), name='all-products'),
    path('product/<str:pslug>/', ProductDetailAPIView.as_view(), name='product'),
    path('brand/', BrandAPIView.as_view(), name='brand'),
]
