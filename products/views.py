from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product
from .choices import lighting_choices, scents_candles, home_decor, electronics

def index(request):
    products = Product.objects.order_by('-id').filter(is_published=True)

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    return render(request, 'products/product.html', context)

def search(request):
    queryset_list = Product.objects.order_by('-id').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords, title__icontains=keywords)

    context = {
        'products': queryset_list,
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    return render(request, 'products/search.html', context)

def category(request, category):

    queryset_list = Product.objects.filter(category=category)

    context = {
        'products': queryset_list,
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    return render(request, 'products/category.html', context)
