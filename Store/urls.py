from django.urls import path
from django.urls import path

from .views import Cart, Login, Signup, Home, Checkout, Orders

urlpatterns = [

        path('', Home.as_view(), name='home'),
        path('signup/', Signup.as_view(), name='signup'),
        path('login/', Login.as_view(), name='login'),
        path('logout/', Login.as_view(), name='logout'),
        path('orders/', Orders.as_view(), name='orders'),
        path('cart/', Cart.as_view(), name='cart'),
        path('checkout/', Checkout.as_view(), name='checkout'),

]