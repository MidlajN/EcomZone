from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['password1']

        if password == conf_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('EcomCredential:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('EcomCredential:register')

            else:
                user = User.objects.create_user(
                    username=user_name, first_name=first_name, last_name=last_name,
                    password=password, email=email
                )
                user.save()
                messages.info(request, 'Welcome')
        else:
            messages.info(request, 'Password not matched')
            return redirect('EcomCredential:register')

        return redirect('/')
    return render(request, 'registration.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('EcomCredential:login')
    return render(request, 'login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/')
