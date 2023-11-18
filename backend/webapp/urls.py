from django.urls import path
from .views import AllProductsAPIView, TopRatedAPIView

urlpatterns = [
    path('products/', AllProductsAPIView.as_view(), name='products'),
    path('products/top-rated', TopRatedAPIView.as_view(), name='top-rated'),
]
