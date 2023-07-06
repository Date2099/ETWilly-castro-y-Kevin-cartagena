from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Sale(models.Model):
    date = models.DateTimeField(default=datetime.now())
    client = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    if_offer = models.BooleanField()
    discount_percent = models.IntegerField()
    image = models.CharField(max_length=200)

    def get_discount_price(self):
        return self.price - (self.price * self.discount_percent) / 100




class Detail(models.Model):
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()


class Following(models.Model):
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())







