from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
	path('', views.index, name='index'),
	path('products/', views.index, name='products'),
	path('products/<int:id>/', views.product_detail, name='detail'),
]
