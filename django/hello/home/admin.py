from django.contrib import admin

from home.models import Contact, Product, Category, Order

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
