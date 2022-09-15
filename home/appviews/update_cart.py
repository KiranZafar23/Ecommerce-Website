from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class UpdateCart(View):
    def post(self, request, retailer_sku, availability):
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart')
        
        cart[product] = quantity
        request.session['cart'] = cart

        products = convert_to_json(Product.objects.filter(retailer_sku=retailer_sku))
        context = {'product': products[0], 'availability':availability}

        return render(request, 'productdetail.html', context)
