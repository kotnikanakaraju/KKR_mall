from django.shortcuts import render
from . models import store,product

def store_detail(request,store_id):
    store =store.objects.get(pk=store_id)
    products=product.objects.filter(store=store)
    return render(request,'shop/store_detail.html',{'store':store,'products':products})
