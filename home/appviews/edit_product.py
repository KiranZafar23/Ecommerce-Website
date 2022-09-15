from django.shortcuts import render
from django.views import View

from home.models.product import Product


class EditProduct(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}

        return render(request, 'product.html', context)
