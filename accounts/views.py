from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from products.choices import lighting_choices, scents_candles, home_decor, electronics

def register(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)

def login(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('my_account')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def my_account(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }
    return render(request, 'accounts/my_account.html', context)

