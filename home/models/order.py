import datetime

from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=10)
    product = models.CharField(max_length=50000)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    image = models.TextField(default='')

    @staticmethod
    def get_orders_by_user(name):
        return Order.objects.filter(name=name).order_by('-date')

    def __str__(self):
        return self.name
