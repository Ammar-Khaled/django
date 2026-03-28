from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1  # to get the category object
        read_only_fields = ['id']

    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Category with that ID does not exist.")
        return value

    # def create(self, validated_data):
    #     product = Product.objects.create(**validated_data)
    #     return product

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.stock = validated_data.get('stock', instance.stock)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)
    #     instance.save()
