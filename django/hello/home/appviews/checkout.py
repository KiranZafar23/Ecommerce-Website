from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from home.models.order import Order
from home.models.product import Product


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        name = request.user
        cart = request.session.get('cart')
        products = Product.get_products_by_retailer_sku(list(cart.keys()))

        for product in products:
            order = Order(name=name, product=product, image=product.image_urls, price=product.price, address=address,
                          phone=phone, quantity=cart.get(str(product.retailer_sku)))
            order.save()
    
        messages.success(request, f"{name}, Thanks for Your Order")
        request.session['cart'] = dict()

        return redirect('cart')
