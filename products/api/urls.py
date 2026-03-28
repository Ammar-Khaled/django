from django.urls import path
from products.api.views import index, product

urlpatterns = [
    path('index', index, name='products.api.index'),
    path('<int:pk>/', product, name='products.api.product'),
]