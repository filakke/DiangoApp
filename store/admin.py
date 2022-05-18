from django.contrib import admin

from store.models import ProductApp, Order, Cart


# Register your models here.
admin.site.register(ProductApp)
admin.site.register(Order)
admin.site.register(Cart)