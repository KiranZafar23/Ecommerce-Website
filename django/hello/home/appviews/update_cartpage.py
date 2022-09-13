from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class UpdateCartPage(View):
    def post(self, request):
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart')
        
        cart[product] = quantity
        request.session['cart'] = cart


        cart_ids = list(request.session.get('cart').keys())
        products = convert_to_json(Product.get_products_by_retailer_sku(cart_ids))

        return render(request, 'cart.html', {'products': products})
       