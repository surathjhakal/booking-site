from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import MySiteUser
from django.urls import reverse
# Create your views here.


def index(request):
    if not request.session.has_key('uid'):
        return redirect('sign_in')
    return render(request, 'booking/index.html')


def sign_up(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        number = request.POST['user_number']
        password = request.POST['user_password']
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
                                      password=password)
                new_user.save()
                return render(request, 'booking/signupPage.html', context={'message': 'You have created your account successfully, Now Sign In'})
    return render(request, 'booking/signupPage.html', {'message': ''})


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_password']
        try:
            user = MySiteUser.objects.get(email=email)
            if user.password == password:
                # file = open('booking/allow.txt', 'w')
                # file.write('True')
                request.session['uid'] = request.POST['user_email']
                return redirect('index')
            else:
                return render(request, 'booking/signinPage.html', {'message': 'Invalid password entered'})
        except:
            return render(request, 'booking/signinPage.html', {'message': 'There is no user with this mail'})
    return render(request, 'booking/signinPage.html', {'message': ''})


def log_out(request):
    # file = open('booking/allow.txt', 'r')
    # data = file.read()
    del request.session['uid']
    return redirect('index')
