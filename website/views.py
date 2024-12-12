from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check login logic here
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Authenticated Successfully')
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials...")
            return redirect('home')
    
    # if user is already logged in
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})