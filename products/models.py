from django.db import models
from categories.models import Category

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/products", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    @property
    def image_url(self):
        return f'/media/{self.image}'