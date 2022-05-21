
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import os
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def index(request):

    mdl_obj = ProductModel.objects.all()
    return render(request, 'index.html', {'inc': mdl_obj})


@login_required(login_url='login')
def detail_view(request, pk):
    var = ProductModel.objects.filter(id=pk)

    return render(request, 'details.html', {'xx': var})


def signupFun(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']

        # auth_user_fields_on_top
        zipcode = request.POST['zip']
        place = request.POST['place']
        address = request.POST['addr']
        gender = request.POST['gen']
        phone = request.POST['ph']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already exists...!!')
                return redirect('signupFun')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already registerd..!!')
                return redirect('signupFun')
            else:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pwd,
                    email=email,
                )
                user.save()
                u = User.objects.get(id=user.id)  # for fkey
                extra = UserEx(
                    user=u,  # fkey
                    zipcode=zipcode,
                    place=place,
                    address=address,
                    gender=gender,
                    mobile=phone,
                    image=image,
                )
                extra.save()
                return redirect('login')
        else:
            messages.info(request, 'paswd doesnt match..!!')
            return redirect('signupFun')
    return render(request, 'signup.html')


def login(request):
    try:
        if request.method == 'POST':
            uname = request.POST['uname']
            pwd = request.POST['pswd']
            user = auth.authenticate(username=uname, password=pwd)

            if user is not None:
                if user.is_superuser:
                    request.session['uid'] = user.id
                    auth.login(request, user)
                    return redirect('dashboard')
                else:
                    request.session['uid'] = user.id
                    auth.login(request, user)
                    # messages.info(request, f'Welcome{uname}')
                    return redirect('/')
            else:
                messages.info(
                    request, 'Invalid Username or Password. Try Again.IN')
                return redirect('login')

        return render(request, 'login.html')
    except:
        # messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')


def logout(request):
    request.session['uid'] = ''
    auth.logout(request)
    return redirect('/')


def add_category(request):
    if request.method == 'POST':
        ct = request.POST['cat']

        mdl = ProductCategory(
            category=ct
        )
        mdl.save()
        return redirect('dashboard')
    return render(request, 'a_new_cat.html')


@login_required(login_url='login')
def cart(request):

    try:

        var = CartModel.objects.filter(user=request.user)

        if len(set(var)) <= 0:
            messages.info(request, ' cart is Empttyyy')
            return render(request, 'cart.html')

        else:
            context = {
                'var': var
            }
            return render(request, 'cart.html', context)

    except:
        messages.info(request, 'something wrong')
        return redirect('/')


def add_to_cart(request, pk):
    if 'uid' in request.session:
        usr = request.user
        var = ProductModel.objects.get(id=pk)
        obj = CartModel(
            prdt=var,
            user=usr,

        )
        obj.save()
        return redirect('cart')
    else:
        return redirect('login')


@login_required(login_url='login')
def remove_cart(request, pk):

    pr = CartModel.objects.get(id=pk)
    pr.delete()
    return redirect('cart')

    return render(request, 'cart.html')


@login_required(login_url='login')
def shop_panel(request):

    var = ProductCategory.objects.all()

    var1 = ProductModel.objects.all()
    context = {
        'ii': var,
        'iii': var1
    }

    return render(request, 'shop.html', context)
#---------User_profile-----__#


def profile(request):
    n = request.user
    print(n)
    var = UserEx.objects.filter(user=n)

    return render(request, 'profile.html', {'var': var})

# ----------------------Category Filters--------------#


def laptop_filter(request):
    var = ProductCategory.objects.get(category='Laptop')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


def tv_filter(request):
    var = ProductCategory.objects.get(category='TV')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


def home_filter(request):
    var = ProductCategory.objects.get(category='Home')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


def fitness_filter(request):
    var = ProductCategory.objects.get(category='Fitness')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


def redmi_filter(request):
    var = ProductCategory.objects.get(category='Redmi Phones')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


def audio_filter(request):

    var = ProductCategory.objects.get(category='Audio')
    var1 = ProductModel.objects.filter(category=var)

    context = {
        'obj': var1
    }
    return render(request, 'list.html', context)


#-----------Filter_ends----------------#
@login_required(login_url='login')
def about(request):
    return render(request, 'aboutus.html')


#-----------DASHBOARD---------------------#
def dashboard(request):

    if request.method == 'POST':
        ct = request.POST['category']
        filter_fkey = ProductCategory.objects.get(id=ct)
        pname = request.POST['pname']
        tit = request.POST['tt']
        des = request.POST['des']
        pri = request.POST['price']
        qty = request.POST['qty']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"

        obj = ProductModel(

            category=filter_fkey,
            product_name=pname,
            product_title=tit,
            description=des,
            price=pri,
            quantity=qty,
            image=image


        )
        obj.save()
        return redirect('dashboard')

    usrs = UserEx.objects.all()
    products = ProductModel.objects.all()
    obj = ProductCategory.objects.all()
    context = {
        'usr': usrs,
        'obj': obj,
        'products': products,
    }

    return render(request, 'dashboard.html', context)


def delete_usr(request, pk):
    ur = UserEx.objects.get(id=pk)
    ur.delete()
    return redirect('dashboard')


def admin_cart_view(request, pk):
    try:

        var = CartModel.objects.filter(user=pk)
        print(pk)

        if len(set(var)) <= 0:
            messages.info(request, ' cart is Empttyyy')
            return render(request, 'cart.html')

        else:
            context = {
                'var': var
            }
            return render(request, 'cart.html', context)

    except:
        messages.info(request, 'something wrong')
        return redirect('/')


def ProductModelEdit(request, pk):

    if request.method == 'POST':
        ct = request.POST['category']
        filter_fkey = ProductCategory.objects.get(id=ct)
        pname = request.POST['pname']
        tit = request.POST['tt']
        des = request.POST['des']
        pri = request.POST['price']
        qty = request.POST['qty']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"
        obj = ProductModel(

            category=filter_fkey,
            product_name=pname,
            product_title=tit,
            description=des,
            price=pri,
            quantity=qty,
            image=image


        )
        obj.save()
        return redirect('dashboard')

    obj = ProductCategory.objects.all()
    pro = ProductModel.objects.filter(id=pk)
    print(set(pro))
    context = {
        'obj': obj,
        'pro': pro
    }
    return render(request, 'editproducts.html', context)



def delete_product(request, pk):
    ur = ProductModel.objects.get(id=pk)
    ur.delete()
    return redirect('dashboard')