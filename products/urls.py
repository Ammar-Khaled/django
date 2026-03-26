from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
	path('', views.index, name='index'),
	path('products/', views.index, name='products'),
	path('products/create/', views.create_product, name='create'),
	path('products/<int:id>/update/', views.update_product, name='update'),
	path('products/<int:id>/', views.product_detail, name='detail'),
	path('products/<int:id>/delete/', views.delete_product, name='delete'),
	path('categories/', views.categories, name='categories'),
	path('categories/<int:id>/', views.category_detail, name='category_detail'),
]
