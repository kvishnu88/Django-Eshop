from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Order, Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .middlewares.auth import  auth_middleware
from django.utils.decorators import method_decorator

# Create your views here.

class Home(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products  = None
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_categoryid(category_id)
        else:
            products = products = Product.get_all_products()
        return render(request, 'home.html',{'products':products,'categories':categories})

    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity >= 0:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        products = Product.get_all_products()
        categories = Category.objects.all()
        return render(request, 'home.html',{'products':products,'categories':categories})

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(sefl, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            cust = Customer.objects.filter(email=email)
            if check_password(password, cust[0].password):
                request.session['customer_id'] = cust[0].id
                request.session['email'] = cust[0].email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                Login.return_url = None
                return redirect('home')
            else:
                return render(request, 'login.html',{'user':'Invalid username or password!!! '})
        except Exception:
            return render(request, 'login.html',{'user':'User does not exists...'}) 

def logout(request):
    request.session.clear()
    redirect('login')


class Signup(View):    
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        values = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone
            }
            
        if password == confirm_password:
            password = make_password(password)
            cust = Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
            if cust.isExist(): 
                return render(request, 'signup.html',{'values':values,'email_exit_error':'Email alrady exist'})
            else:
                cust.save()
            return redirect('home')
        else:
            return render(request, 'signup.html',{'alert':'Password is not matched','values':values})
    
    def validateCustmer(Customer):
        if Customer.first_name:
            first_name_empty = 'First name required'
        elif len(Customer.first_name)> 1:
            first_name_small = 'First name must be greater then 1 character'
        if Customer.last_name:
            last_name_empty = 'Last name required'
        elif len(Customer.last_name)>1:
            last_name_small = 'Last name must be greater then 1 character'
        if Customer.email:
            email_empty = 'Email required'
        if len(Customer.phone) == 10:
            phone_size = 'Phone number must be 10 digit'
        
class Cart(View):
    def get(self, request):
        ids = ''
        products = ''
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            products = Product.objects.filter(id__in=ids)
        else:
            request.session['cart'] = {}
        return render(request, 'cart.html',{'products':products})

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cust = request.session.get('customer_id')
        cart = request.session.get('cart')
        ids = list(cart.keys())
        products = Product.objects.filter(id__in=ids)
        print(cust,products[0].id)
        for product in products:
            order = Order(customer = Customer(id=cust), 
                            product=product,
                            price = product.price,
                            address = address,
                            phone = phone,
                            quantity = cart.get(str(product.id))
                    )
            if request.session.get('customer_id'):
                order.save()
            else:
                return redirect('login')
        request.session['cart'] = {}
        return redirect('cart')

class Orders(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer_id')
        orders  = Order.objects.filter(customer_id= customer).order_by('-dated')
        return render(request, 'orders.html',{'orders': orders})