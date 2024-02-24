from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from enrollment.models import Registration
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.
def enrollment_view(request):
    registers = Registration.objects.all()

    paginator = Paginator(registers, 10)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    registers = Registration.objects.filter(
        Q(
            Q(name__icontains=search_term) | # "OR" in database
            Q(sig_register__icontains=search_term),
        ),
    ).order_by('-id')


    paginator = Paginator(registers, 10)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page,
    })

def add_view(request):
    if request.user.is_authenticated:
        return redirect('users:menu')

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Adicionar',
            'form_action': reverse('enrollment:add_create'), # change here
    })


