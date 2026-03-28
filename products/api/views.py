# get all products
from rest_framework.decorators import api_view
from products.models import Product
from products.api.serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products = ProductSerializer(products, many=True).data
        
        # build the image url for each product 
        for product in products:        
            product['image'] = request.build_absolute_uri(product['image'])

        return Response(products)
    
    # POST
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response({'product': product.data, 'message': 'Product created successfully'}, status=201)

    return Response({'message': 'failed to create product', 'errors': product.errors}, status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        data = ProductSerializer(product).data
        # build absolute image URL if present
        if data.get('image'):
            data['image'] = request.build_absolute_uri(data['image'])
        return Response(data)

    if request.method == 'PATCH':
        prodcut = ProductSerializer(product, data=request.data)
        if prodcut.is_valid():
            prodcut.save()
            data = prodcut.data
            if data.get('image'):
                data['image'] = request.build_absolute_uri(data['image'])
            return Response({'product': data, 'message': 'Product updated successfully'})
        return Response({'message': 'failed to update product', 'errors': prodcut.errors}, status=400)

    # DELETE
    product.delete()
    return Response({'message': 'Product deleted successfully'}, status=204)