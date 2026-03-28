from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from categories.models import Category
from categories.api.serializers import CategorySerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data

        # build absolute logo URL
        for cat in data:
            if cat.get('logo'):
                cat['logo'] = request.build_absolute_uri(cat['logo'])

        return Response(data)

    category = CategorySerializer(data=request.data)
    if category.is_valid():
        category.save()
        data = category.data
        if data.get('logo'):
            data['logo'] = request.build_absolute_uri(data['logo'])
        return Response({'category': data, 'message': 'Category created successfully'}, status=201)

    return Response({'message': 'failed to create category', 'errors': category.errors}, status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
def category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        data = CategorySerializer(category).data
        if data.get('logo'):
            data['logo'] = request.build_absolute_uri(data['logo'])
        return Response(data)

    if request.method == 'PATCH':
        category = CategorySerializer(category, data=request.data)
        if category.is_valid():
            category.save()
            data = category.data
            if data.get('logo'):
                data['logo'] = request.build_absolute_uri(data['logo'])
            return Response({'category': data, 'message': 'Category updated successfully'})
        return Response({'message': 'failed to update category', 'errors': category.errors}, status=400)

    category.delete()
    return Response({'message': 'Category deleted successfully'}, status=204)