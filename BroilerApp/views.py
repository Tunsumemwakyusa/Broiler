from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    # user = User.objects.get(user_id=request.user.id)
    # username = user.username
    # email = user.email
    # context = {
    #     'username': username,
    #     'email': email,
    # }
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.authenticate(email=email, password=password)
            auth.login(request, user)
            messages.success(request, 'You Loged In')
            return redirect('to_do_list')
        # else:
        #    messages.error(request, 'Invarid credentials')
        #    return redirect('login')
        except:
            messages.error(request, 'Your not registered please reister')

    return render(request, 'login.html')


@login_required(login_url='login')
def to_do_list(request):
    return render(request, 'to_do_list.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You logged out')
    return redirect('index')
