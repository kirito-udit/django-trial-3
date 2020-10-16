from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from django.http import JsonResponse
from vid2 import urls
import time

def login_page(request):
    time.sleep(3)
    return render(request, 'signin.html')

def intro(request):
    return render(request, 'intro.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('/user')
        else:
            error = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'signin.html', {'error': error})
    else:
        return render(request, 'signin.html')


def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request,'logout.html')


