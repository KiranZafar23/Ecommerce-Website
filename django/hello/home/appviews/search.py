from django.contrib import messages
from django.shortcuts import render
from django.views import View

from home.models.product import Product


class Search(View):
    def get(self, request):
        query = request.GET['query']
        products_name = Product.objects.filter(name__icontains=query)
        products_color = Product.objects.filter(color__icontains=query)
        products_gender = Product.objects.filter(gender__icontains=query)
        query_products = products_name.union(products_color, products_gender)

        if query_products.count() == 0:
            messages.warning(request, "No search results found. Please refine your query.")

        query_result = {'query_products': query_products, 'query': query}

        return render(request, 'search.html', query_result)
