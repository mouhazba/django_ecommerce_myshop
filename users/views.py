from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Managers


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = Managers.objects.create_user(email=email, username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')

"""
 LOGIN_REDIRECT_URL = 'home' equivalent à
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'signup.html')"""


"""
LOGOUT_REDIRECT_URL = 'home' est equivalent à
def logout_user(request):
    logout(request)
    return redirect('index')
"""