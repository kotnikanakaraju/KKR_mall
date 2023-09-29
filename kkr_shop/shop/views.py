from django.shortcuts import render
from . models import store,product

def store_list(request):
    stores=store.objects.all()
    return render(request,'shop/list.html',{'stores':stores})

def store_detail(request,store_id):
    store =store.objects.get(pk=store_id)
    products=product.objects.filter(store=store)
    return render(request,'shop/store_detail.html',{'store':store,'products':products})
