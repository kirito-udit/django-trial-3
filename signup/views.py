from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.conf import settings
import socket
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            n = random.randint(3000,7000)
            msg =  'Hey!! Thanks for Registering on Strangeflix, your One Time Paasword is : '
            msg+=str(n)
            usermail = request.user.email
    #socket.getaddrinfo('localhost', 465)
            send_mail(
            'Your StrangeFlix OTP',
            msg,
            'strangeflixkastrangeflex@gmail.com',
            [usermail],
            fail_silently=False,)
            return render(request, 'otp.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup2.html', {'form': form})

def verify(request):
    otp = request.GET['otp']
    n = signup(request)
    if otp == n:
            return redirect('home')
    else :   
        return render(request, 'otp.html',)
