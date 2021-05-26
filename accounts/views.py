from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .forms import LoginFormModelForm, RegisterFormModelForm

User = get_user_model()


def home_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request, 'accounts/home.html', {
        'title': 'Home',
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect("account:home")

    if request.POST:
        form = LoginFormModelForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("account:home")
    else:
        form = LoginFormModelForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def register_view(request):
    if request.POST:
        form = RegisterFormModelForm(request.POST)
        if form.is_valid():
            user = User(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
            )
            user.save()
            user.set_password(request.POST['password1'])
            user.save()
            return redirect("account:home")
    else:
        form = RegisterFormModelForm()

    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("account:login")


def profile_view(request, username):
    user_detail = User.objects.get(username=username)
    context = {
        'title': 'Profile',
        'user_detail': user_detail,
    }
    return render(request, 'accounts/profile.html', context)
