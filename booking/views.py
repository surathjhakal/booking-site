from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MySiteUser
# Create your views here.


def index(request):
    return render(request, 'booking/index.html')


def sign_up(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        number = request.POST['user_number']
        password = request.POST['user_password']
        password_again = request.POST['user_password_again']
        try:
            user = MySiteUser.objects.get(email=email)
            return render(request, 'booking/signupPage.html', {'message': 'This email id is already registered'})
        except:
            try:
                user = MySiteUser.objects.get(number=number)
                return render(request, 'booking/signupPage.html', {'message': 'This phone number is already registered'})
            except:
                print("found")
                new_user = MySiteUser(name=name, email=email, number=number,
                                      password=password, password_again=password_again)
                new_user.save()
                return render(request, 'booking/signupPage.html', context={'message': 'You have created your account successfully, Now Sign In'})
    return render(request, 'booking/signupPage.html', {'message': ''})


def sign_in(request):
    return render(request, 'booking/signinPage.html')
