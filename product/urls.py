from django.urls import path 

from .views import *


urlpatterns = [
    path('', CategoryAPIView.as_view(), name='all-category'),
    path('<str:cslug>/', CategoryDetailAPIView.as_view(), name='category-detail'),
]
