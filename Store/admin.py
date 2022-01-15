from django.contrib import admin
from Store.models import Product, Category, Customer, Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','desc','category']

admin.site.register(Product, AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category, AdminCategory)


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','password']

admin.site.register(Customer, AdminCustomer)

# class AdminOrder(admin.ModelAdmin):
#     list_display = ['quantity','price','customer_id','product_id','dated','phone','address','status']

admin.site.register(Order)
