from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from user import views as auth_views
from product import views as product_views


urlpatterns = [
    # TODO : user app
    path('user/token/', auth_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/auth/', auth_views.AuthAPIView.as_view()),
    path('user/register/', auth_views.RegisterAPIView.as_view()),

    # TODO : 
    path('category/', product_views.CategoryListAPIView.as_view()),
    path('product/', product_views.ProductListAPIView.as_view()),
]
