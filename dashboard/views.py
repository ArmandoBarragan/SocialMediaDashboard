from django.shortcuts import render, redirect, reverse
from dashboard.forms import UserForm, LoginForm
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from dashboard.models import User

# Create your views here.
def index_view(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    return redirect('login')

def login_view(request):
    context = {'form': LoginForm}
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('index')
            else:
                print('something went wrong')
            
            
    return render(request, 'authentication/login.html', context)
    

def creation_view(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect(reverse(index_view))
        
    context = {'form': UserForm}
    return render(request, 'authentication/create.html', context)

def logout(request):
    do_logout(request)
    return redirect('login')