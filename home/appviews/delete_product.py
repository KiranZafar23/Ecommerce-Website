from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from home.models.product import Product


class DeleteProduct(View):
    def get(self, request, retailer_sku, filter):
        product = Product.objects.filter(retailer_sku=retailer_sku)
        product.delete()
        messages.info(request, "Deleted a Product")

        return redirect(f'/products/{filter}')
