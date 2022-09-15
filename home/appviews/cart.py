from django.shortcuts import render
from django.views import View

from home.models.product import Product
from home.utils import convert_to_json


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')

        if not cart:
            request.session['cart'] = dict()

        cart_ids = list(request.session.get('cart').keys())
        products = convert_to_json(Product.get_products_by_retailer_sku(cart_ids))

        return render(request, 'cart.html', {'products': products})
