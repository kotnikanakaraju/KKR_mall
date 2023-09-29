from django.contrib import admin

from .models import store,product,customer,order

@admin.register(store)
class storeAdmin(admin.ModelAdmin):
    list_display=('name','location')


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=('name','store','price')
    list_filter=('store',)

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display=('name','email')

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display=('customer','amount','order_date')

