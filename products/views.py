from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def product_detail(request, id):
    p = get_object_or_404(Product, id=id)
    return render(request, 'products/detail.html', {'product': p})


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get("image")
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')

        product = Product(
            name=name,
            price=price,
            description=description,
            image=image,
            stock=stock,
            category_id=category_id,
        )
        product.save()
        return redirect('products:detail', id=product.id)

    categories = Category.objects.all()
    return render(request, 'products/create_product.html', {'categories': categories})


def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.stock = request.POST.get('stock')
        product.category_id = request.POST.get('category')

        image = request.FILES.get("image")
        if image:
            product.image = image

        product.save()
        return redirect('products:detail', id=product.id)

    categories = Category.objects.all()
    selected_category_id = product.category_id if product.category_id else None
    return render(
        request,
        'products/update_product.html',
        {
            'categories': categories,
            'product': product,
            'selected_category_id': selected_category_id,
        },
    )

def categories(request):
    categories = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'products/category_detail.html', {'category': category})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products:index')
