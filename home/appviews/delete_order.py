from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from home.models.order import Order


class DeleteOrder(View):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        order.delete()
        messages.success(request, "Your order has been deleted")

        return redirect('/orders')
