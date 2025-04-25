from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:id>/', views.product, name='product'),
    path('product_details/<str:cname>/<str:pname>/', views.product_detail, name='product_detail'),
    path('payment/', views.payment, name='payment'),
]
