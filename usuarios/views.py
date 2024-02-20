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
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 'usuarios/pages/register_view.html', {
            'form': form,
            'title': 'Resgistrar',
            'form_action': reverse('usuarios:register_create'),
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
        return redirect(reverse('usuarios:register'))
    
    return redirect('usuarios:register')

def login_view(request):
    form = LoginForm()
    return render(request, 'usuarios/pages/login_view.html', {
        'form': form,
        'title': 'Login',
        'form_action': reverse('usuarios:login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('usuarios:login')

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
    
    return redirect(login_url)

@login_required(login_url='usuarios:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect('usuarios:login')
    
    if request.POST.get('username') != request.user.username:
        return redirect('usuarios:login')
    
    logout(request)
    return redirect(reverse('usuarios:login'))