from django.db import models


class Product(models.Model):
    retailer_sku = models.CharField(primary_key=True, max_length=22)
    brand = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    url = models.URLField()
    color = models.CharField(max_length=122)
    currency = models.CharField(max_length=122)
    status = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    care = models.TextField()
    category = models.TextField()
    description = models.TextField()
    image_urls = models.TextField()

    skus = models.TextField()

    @staticmethod
    def get_products_by_retailer_sku(ids):
        return Product.objects.filter(retailer_sku__in=ids)

    def __str__(self):
        return self.name
