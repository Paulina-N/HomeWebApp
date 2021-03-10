from django.shortcuts import render
from django.http import HttpResponse
from products.choices import lighting_choices, scents_candles, home_decor, electronics
from products.models import Product

def index(request):
    products = Product.objects.order_by('-id').filter(is_published=True)
    context = {
        'products': products,
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }
    return render(request, 'pages/about.html', context)

def products(request):
    return render(request, 'pages/products.html')

def product(request):
    return render(request, 'pages/product.html')

def wishlist(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }
    return render(request, 'pages/wishlist.html', context)

def share_your_ideas(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }
    return render(request, 'pages/share_your_ideas.html', context)
