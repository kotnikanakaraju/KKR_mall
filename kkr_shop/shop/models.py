from django.db import models

class store(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    location=models.CharField(max_length=100)

class product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    store=models.ForeignKey(store,on_delete=models.CASCADE)

class customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

class order(models.Model):
    customer=models.ForeignKey(customer, on_delete=models.CASCADE)
    products=models.ManyToManyField(product)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    order_date=models.DateField(auto_now_add=True)

