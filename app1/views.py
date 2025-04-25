from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app1.form import CustomUserForm
from .models import Category, Product



def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products})



def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        messages.error(request, 'Login failed, please try again.')
        return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    qty = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})

    pid = str(product_id)
    if pid in cart:
        cart[pid]['quantity'] += qty
    else:
        cart[pid] = {
            'quantity': qty,
            'price': float(product.sale_price),  
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for pid, data in cart.items():
        product = get_object_or_404(Product, pk=pid)
        line_total = product.sale_price * data['quantity']
        total += line_total

        items.append({
            'product': product,
            'quantity': data['quantity'],
            'line_total': line_total,
        })

    context = {
        'cart_items': items,
        'cart_total': total,
    }
    return render(request, 'cart.html', context)

def remove_from_cart(request, product_id):
    
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

def register(request):
    form = CustomUserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Registration successful! You can log in now.')
        return redirect('login')
    return render(request, 'register.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')



def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_details.html', {'product': product})  # corrected filename


def product_detail(request, cname, pname):
    category = get_object_or_404(Category, name=cname)
    try:
        product_obj = Product.objects.get(name=pname, category=category)
    except Product.DoesNotExist:
        messages.error(request, 'No Such Product Found')
        return redirect('home')
    return render(request, 'product_details.html', {'product': product_obj})  # consistent filename


def payment(request):
    return render(request, 'payment.html')