from django.shortcuts import render, redirect, reverse
from dashboard.forms import UserForm
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from dashboard.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


def index_view(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('login')


def login_view(request):
    context = {'form': AuthenticationForm}

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('index')
            else:
                context = {'form': form}
                if form.errors:
                    print(form.errors)

    return render(request, 'authentication/login.html', context)


def creation_view(request):
    context = {'form': UserForm}
    if request.method == "POST":
        form = UserForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            do_login(request, user)
            return redirect(reverse(index_view))
        else:
            context = {'form': form}

    return render(request, 'authentication/create.html', context)


def logout(request):
    do_logout(request)
    return redirect('login')
