from operator import mod
from statistics import mode
from django.db import models
from django.db.models.fields.related import ForeignKey
import datetime
from django.utils import timezone 


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.first_name

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    dated = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)
