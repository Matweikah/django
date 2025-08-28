from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # Добавляем импорт
from .models import Podsh, Price

def product_list(request):
    # Получаем все товары
    products_list = Podsh.objects.all()
    
    # Фильтрация по категории (если нужно)
    category = request.GET.get('category')
    if category:
        products_list = products_list.filter(category=category)
    
    # Поиск по названию
    search_query = request.GET.get('search')
    if search_query:
        products_list = products_list.filter(POLN__icontains=search_query)
    
    # Пагинация - 12 товаров на страницу
    paginator = Paginator(products_list, 96)
    page_number = request.GET.get('page')
    
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page не integer, показываем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # Если page вне диапазона, показываем последнюю страницу
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Podsh, ID=product_id)
    
    # Получаем предложения цен для этого товара (ИСКЛЮЧАЕМ цену 0)
    price_offers = Price.objects.filter(bearing=str(product.ID), cena__gt=0).order_by('cena')
    
    # Группируем предложения по поставщикам
    offers_by_seller = {}
    for offer in price_offers:
        if offer.sales not in offers_by_seller:
            offers_by_seller[offer.sales] = []
        offers_by_seller[offer.sales].append(offer)
    
    # Расширяем контекст данными о предложениях
    context = {
        'product': product,
        'price_offers': price_offers,
        'offers_by_seller': offers_by_seller,
        'total_offers': price_offers.count(),
        'min_price': price_offers.first().cena if price_offers else 0,
        'max_price': price_offers.last().cena if price_offers else 0,
    }
    
    return render(request, 'shop/product_detail.html', context)

def category_products(request, category_name):
    products = Podsh.objects.filter(category=category_name)
    return render(request, 'shop/category.html', {
        'products': products,
        'category': category_name
    })