from django.shortcuts import render, redirect, get_object_or_404
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
    registers = Registration.objects.all().order_by('name')

    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)
    
    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page,
        'form_action_search': reverse('enrollment:search'),
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
    ).order_by('name')


    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page,
    })

def add_view(request):
    register_form_data = request.session.pop('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Adicionar',
            'form_action': reverse('enrollment:add_create'),
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

        messages.success(request, 'O usuário foi salvo.')

        del(request.session['register_form_data'])
        return redirect(reverse('enrollment:add_view'))
    
    return redirect('enrollment:add_view')

def to_view(request, id):
    enrollment = Registration.objects.filter(
        pk=id
    ).order_by('name').first()

    form = RegisterForm(instance=enrollment)

    for field_name, field in form.fields.items():
        field.widget.attrs['disabled']=True
        add_attr(form.fields[field_name], 'class', 'disabled') 

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Informações da Matrícula',
            'enrollment': enrollment
    })

def to_edit(request, id):
    enrollment = get_object_or_404(Registration, pk=id)
    
    register_form_data = request.session.pop('register_form_data', None)
    form = RegisterForm(register_form_data, instance=enrollment)
    
    url_parameter = reverse('enrollment:edit_create', kwargs={'id': enrollment.id})
    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Atualizar Matrícula',
            'enrollment': enrollment,
            'form_action': url_parameter,
    })
    
def edit_create(request, id):
    if not request.POST:
        raise Http404()
    
    enrollment = get_object_or_404(Registration, pk=id)
    form = RegisterForm(request.POST, instance=enrollment)
    
    url_parameter = reverse('enrollment:to_edit', kwargs={'id': enrollment.id})
    
    if form.is_valid():
        print(enrollment.name)
        enrollment = form.save(commit=False)
        enrollment.cpf = form.cleaned_data['cpf']
        form.save()

        messages.success(request, 'O usuário foi salvo.')
        return redirect(url_parameter)
    
    request.session['register_form_data'] = request.POST
    return redirect(url_parameter)

def delete_create(request, id):
    # add here later: request.<is_avaliador, is_admin>
    
    enrollment = get_object_or_404(Registration, pk=id)
    name = enrollment.name
    enrollment.delete()

    messages.success(request, f'A matrícula do(a) {name} foi deletada!')
    
    return redirect(reverse('enrollment:enrollment_view'))