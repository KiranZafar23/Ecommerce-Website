from django.shortcuts import redirect
from django.views import View

from home.models.product import Product


class HideShowProduct(View):
    def get(self, request, retailer_sku, filter):
        product = Product.objects.get(retailer_sku=retailer_sku)

        if product.status:
            product.status = False
        else:
            product.status = True

        product_detail = Product(retailer_sku=retailer_sku, brand=product.brand, name=product.name, color=product.color,
                                 gender=product.gender, category=product.category, price=product.price, url=product.url,
                                 description=product.description, care=product.care, image_urls=product.image_urls,
                                 currency=product.currency, skus=product.skus, status=product.status)
        product_detail.save()
        print(product.status)

        return redirect(f'/products/{filter}')
