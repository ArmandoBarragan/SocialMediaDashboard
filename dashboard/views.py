from django.shortcuts import render, redirect, reverse
from dashboard.forms import UserForm, LoginForm
# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    context = {'form': LoginForm}
    print('buenas')
    return render(request, 'authentication/login.html', context)

def login(request, user):
    pass

def creation_view(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect(reverse(login_view))

    context = {'form': UserForm}
    return render(request, 'authentication/create.html', context)

def logout(request):
    pass

