from django.contrib import messages
from django.shortcuts import redirect
from django.views import View


class RemoveCartItem(View):
    def get(self, request, retailer_sku):
        cart = request.session.get('cart', {})
        cart.pop(retailer_sku)
        request.session['cart'] = cart
        messages.success(request, "Item has been removed from cart")

        return redirect('/cart')
