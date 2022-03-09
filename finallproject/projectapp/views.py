from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorations import *
from django.urls import reverse

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=username)
            messages.success(request, 'Аккаун был упешно создан для ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'finallproject/register.html', context)

@login_required(login_url="login")
def favorite_list(request):
    new = Product.objects.filter(favorites=request.user)
    return render(request, 'finallproject/favorites.html', {'new': new})

@login_required(login_url="login")
def main_page(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'finallproject/index.html', context)

@login_required(login_url="login")
def blog(request):
    return render(request, 'finallproject/blog.html')

@login_required(login_url="login")
def cart(request):
    return render(request, 'finallproject/cart.html')

@login_required(login_url="login")
def favorite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user) 
    else:
        product.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def category(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {
        'products': products,
        'myFilter': myFilter,
    }
    
    return render(request, 'finallproject/category.html', context)

@login_required(login_url="login")
def product(request, id):
    products = Product.objects.get(pk=id)
    return render(request, 'finallproject/pr.html', {'products': products })



@login_required(login_url="login")
def contact(request):
    form=SentMessageForm()
    if request.method == 'POST':
        form = SentMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            messages.info(request, "ERORR")

    context={'form': form}

    return render(request, 'finallproject/contact.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.info(request, "ERORR")
            
    context = {}

    return render(request, 'finallproject/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'finallproject/cart.html')

@login_required(login_url="/users/login")
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            form = ProductForm()
        return render(request, 'finallproject/create_product.html',  {'form': form})

    context = {
        'form': form    
    }

    return render(request, 'finallproject/create_product.html', context)

@login_required(login_url="/users/login")
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            form = ProductForm()

    context = {
        'form': form
    }

    return render(request,  'finallproject/update.html', context)

@login_required(login_url="/users/login")
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect ('category')

    context={'item': product}
    return render (request, 'finallproject/delete_pr.html', context)

@login_required(login_url="/users/login")
def user_profile(request):
    pass

@login_required(login_url="/users/login")
def profile(request, pk_test):
    profile = Customer.objects.get(id=pk_test)

    context = {'profile': profile}

    return render(request, 'finallproject/profile.html', context)
        