from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from user import views as auth_views
from product import views as product_views
from cart import views as cart_views


urlpatterns = [
    # TODO : user app
    path('user/token/', auth_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/auth/', auth_views.AuthAPIView.as_view()),
    path('user/register/', auth_views.RegisterAPIView.as_view()),

    # TODO : product app
    path('category/', product_views.CategoryListAPIView.as_view()),
    path('product/', product_views.ProductListAPIView.as_view()),
    path('product/<str:slug>/', product_views.ProductDetailAPIView.as_view()),

    # TODO : cart app
    path('add/cart/', cart_views.CartAPIView.as_view()),
]
