from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from enrollment.models import Registration
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import RegisterForm
from django.urls import reverse
from django.contrib import messages
from utils.django_forms import add_attr

# Create your views here.
def enrollment_view(request):
    registers = Registration.objects.all()

    paginator = Paginator(registers, 8)
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


    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page,
    })

def add_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Adicionar',
            'form_action': reverse('enrollment:add_create'), # change here
    })


def add_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.save()

        messages.success(request, 'O usuário foi criado.')

        del(request.session['register_form_data'])
        return redirect(reverse('enrollment:add_view'))
    
    return redirect('enrollment:add_view')

def to_view(request, id):
    enrollment = Registration.objects.filter(
        pk=id
    ).order_by('-id').first()

    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    for field_name, field in form.fields.items():
        if hasattr(field, 'choices'):
            field.widget.attrs['disabled']=True
            add_attr(form.fields[field_name], 'class', 'disabled') 
        else:    
            field.widget.attrs['disabled']=True
            add_attr(form.fields[field_name], 'value', getattr(enrollment, field_name))
            add_attr(form.fields[field_name], 'class', 'disabled')

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Informações da Matrícula',
            'enrollment': enrollment
    })
