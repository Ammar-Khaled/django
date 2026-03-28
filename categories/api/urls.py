from django.urls import path
from categories.api.views import index, category

urlpatterns = [
    path('index', index, name='categories.api.index'),
    path('<int:pk>/', category, name='categories.api.category'),
]