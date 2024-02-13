from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 
        'usuarios/pages/register_view.html', {
        'form': form
    })
