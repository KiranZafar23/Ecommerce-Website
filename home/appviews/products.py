from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class Products(View):
    def get(self, request, filter):
        cart = request.session.get('cart')

        if not cart:
            request.session['cart'] = dict()

        if request.user.is_superuser:
            if 'all' in filter.lower():
                products = convert_to_json(Product.objects.all())
            elif 'atoz' in filter.lower():
                products = convert_to_json(Product.objects.all().order_by('name'))
            elif 'ztoa' in filter.lower():
                products = convert_to_json(Product.objects.all().order_by('-name'))  
            elif 'hightolow' in filter.lower():
                products = convert_to_json(Product.objects.all().order_by('-price'))  
            elif 'lowtohigh' in filter.lower():
                products = convert_to_json(Product.objects.all().order_by('price')) 
            else:
                products = convert_to_json(Product.objects.filter(category=filter))    
        else:
            if 'all' in filter.lower():
                products = convert_to_json(Product.objects.filter(status='True'))
            elif 'atoz' in filter.lower():
                products = convert_to_json(Product.objects.filter(status='True').order_by('name'))
            elif 'ztoa' in filter.lower():
                products = convert_to_json(Product.objects.filter(status='True').order_by('-name'))  
            elif 'hightolow' in filter.lower():
                products = convert_to_json(Product.objects.filter(status='True').order_by('-price'))  
            elif 'lowtohigh' in filter.lower():
                products = convert_to_json(Product.objects.filter(status='True').order_by('price')) 
            else:
                products = convert_to_json(Product.objects.filter(status='True', category=filter))        

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {'page_obj': page, 'products': products, 'filter': filter}

        return render(request, 'product.html', context)

