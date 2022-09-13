from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from home.models.product import Product


class UpdateProduct(View):
    def post(self, request, retailer_sku, filter):
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        color = request.POST.get('color')
        gender = request.POST.get('gender')
        price = request.POST.get('price')
        url = request.POST.get('url')
        currency = request.POST.get('currency')

        category = request.POST.get('category')
        description = request.POST.get('description')
        care = request.POST.get('care')
        
        image_urls = list(set(request.POST.getlist('image_urls')))

        raw_size = request.POST.getlist('skusSize')
        raw_stock = request.POST.getlist('skusStock')
        skus=[]

        for size in range(len(raw_size)):
            sku = {}

            if 'true' in raw_stock[size].lower():
                sku['out_of_stock'] =  True
            else:
                sku['out_of_stock'] = False
            sku['size'] = raw_size[size]
            skus.append(sku)
        
        product_detail = Product(retailer_sku=retailer_sku, brand=brand, name=name, color=color, gender=gender,
                                 category=category, price=price, description=description, care=care, url=url,
                                 image_urls=image_urls, currency=currency, skus=skus)
        product_detail.save()
        messages.info(request, "Updated a Product")

        return redirect(f'/products/{filter}')

    def get(self, request):
        return render(request, 'product.html')
