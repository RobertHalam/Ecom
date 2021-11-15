from django.urls import path
from .middlewares.auth import auth_middleware
from .views import Index, OrderView, Signup, Login, logout, Cart, Checkout,Order

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),

]
