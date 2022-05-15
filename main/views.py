import email
from django.shortcuts import render, redirect
import os
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def signupFun(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']

        # auth_user_fields_on_top
        zipcode=request.POST['zip']
        place=request.POST['place']
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
                    zipcode =zipcode,
                    place =place,
                    address=address,
                    gender=gender,
                    mobile=phone,
                    image=image,
                )
                extra.save()
                return redirect('/')
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
                    #messages.info(request, f'Welcome{uname}')
                    return redirect('/')
            else:
                messages.info(
                    request, 'Invalid Username or Password. Try Again.IN')
                return redirect('login')

        return render(request, 'login.html')
    except:
        # messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')




def dashboard(request):


    return render(request,'dashboard.html')






def logout(request):
    request.session['uid'] = ''
    auth.logout(request)
    return redirect('/')
