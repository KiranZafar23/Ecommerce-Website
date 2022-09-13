from django.shortcuts import render
from django.views import View

from home.models.order import Order
from home.utils import imagestring_to_json


class ProductOrders(View):
    def get(self, request):
        customer = request.user

        if request.user.is_superuser:
            orders = imagestring_to_json(Order.objects.all())
        else:    
            orders = imagestring_to_json(Order.get_orders_by_user(customer))

        return render(request, 'orders.html', {'orders': orders})
