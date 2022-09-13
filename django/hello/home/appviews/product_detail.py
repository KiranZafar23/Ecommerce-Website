from inspect import stack
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class ProductDetail(View):
    def get(self, request, retailer_sku):
        try:
            products = convert_to_json(Product.objects.filter(retailer_sku=retailer_sku))
            availability = False

            for stock in products[0]['skus']:
                if not stock['out_of_stock']:
                    availability = True

            context = {'product': products[0], 'availability':availability}
      
            return render(request, 'productdetail.html', context)
                
        except Exception:
            return HttpResponseNotFound()
