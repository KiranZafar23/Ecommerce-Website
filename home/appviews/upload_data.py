from json import load

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views import View

from home.models.product import Product


class UploadData(View):
    def post(self, request):
        uploaded_file = request.FILES['document']
        file = FileSystemStorage()
        file.save(uploaded_file.name, uploaded_file)
        file = open('/home/kiranzafar/project/django/hello/media/ministryofsupply.json', "r")
        products = load(file)

        for product in products:
            product_detail = Product(brand=product['brand'], retailer_sku=product['retailer_sku'], name=product['name'],
                                     gender=product['gender'], description=product['description'], care=product['care'],
                                     category=product['category'], url=product['url'], color=product['color'],
                                     price=product['price'], currency=product['currency'], skus=product['skus'],
                                     image_urls=product['image_urls'])
            product_detail.save()
        messages.success(request, "Your file has been added successfully")

        return render(request, 'uploadfile.html')

    def get(self, request):
        return render(request, 'uploadfile.html')
