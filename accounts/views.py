from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            authenticate(username = username,email = email, password = raw_password )
            messages.success(request,f'Account is Successfully created for {username}!')
            return redirect('accounts:accounts-login')
            
        else:
            context['registration_form'] = form
    else:
        user = request.user
        if user.is_authenticated:
            return redirect('blog:blog-index')
        form = RegistrationForm()
        context['registration_form'] = form
    
    context['h_title'] = 'Sign Up'
    return render(request , 'accounts/register.html' , context)

def logout_view(request):
    logout(request)
    messages.success(request,f'Sucessfully Logged Out')
    return redirect('accounts:accounts-login')


def login_view(request):
    context = {
        'h_title':'Log In'
    }

    user = request.user
    if user.is_authenticated:
        return redirect('blog:blog-index')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request , user)
                messages.success(request,f'Successful Login')
            else:
                messages.warning(request,'Invalid Login')
    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form
    
    return render(request , 'accounts/login.html', context )    