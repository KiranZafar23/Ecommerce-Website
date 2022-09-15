from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class Category(View):
    def get(self, request, category):
        if request.user.is_superuser:
            products = convert_to_json(Product.objects.filter(gender=category))    
        else:
            products = convert_to_json(Product.objects.filter(status='True', gender=category))        

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {'page_obj': page, 'products': products, 'category': category}

        return render(request, 'categories.html', context)

