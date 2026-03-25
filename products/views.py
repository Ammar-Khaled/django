from django.shortcuts import render


products = [
    {
        'id': 1,
        'name': 'wireless-headphones',
        'stock': 12,
        'image': 'images/products/headphones.svg',
        'price': 149.99,
        'description': 'Comfort-fit wireless headphones with noise isolation and 30-hour battery life.',
    },
    {
        'id': 2,
        'name': 'smart-watch',
        'stock': 21,
        'image': 'images/products/watch.svg',
        'price': 89.50,
        'description': 'Lightweight smart watch with heart-rate tracking, sleep insights, and water resistance.',
    },
    {
        'id': 3,
        'name': 'gaming-mouse',
        'stock': 35,
        'image': 'images/products/mouse.svg',
        'price': 59.00,
        'description': 'Ergonomic gaming mouse with RGB lighting, programmable buttons, and precision sensor.',
    },
]


def index(request):
    return render(request, 'products/index.html', {'products': products})


def product_detail(request, id):
    product = None
    for p in products:
        if p['id'] == id:
            product = p
            break

    return render(request, 'products/detail.html', {'product': p})
