from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login, logout
from utils.django_auth import authenticate_by_email
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.user.is_authenticated:
        return redirect('users:menu')

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Registrar',
            'form_action': reverse('users:register_create'),
    })

def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password) # encrypt password
        user.save()

        messages.success(request, 'Usuário criado, você pode fazer login.')

        del(request.session['register_form_data'])
        return redirect(reverse('users:register'))
    
    return redirect('users:register')

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:menu'))

    form = LoginForm()
    return render(request, 'users/pages/login_view.html', {
        'form': form,
        'title': 'Login',
        'form_action': reverse('users:login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate_by_email(
            email=form.cleaned_data.get('email', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'Você foi logado.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais inválidas.')
    else:
        messages.error(request, 'E-mail ou senha inválidos.')
    
    return redirect(reverse('users:menu'))

@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect('users:login')
    
    if request.POST.get('username') != request.user.username:
        return redirect('users:login')
    
    logout(request)
    return redirect(reverse('users:login'))

@login_required(login_url='users:login', redirect_field_name='next')
def menu_view(request):
    return render(request, 'users/pages/menu_view.html')