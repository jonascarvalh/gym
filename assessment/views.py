from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from assessment.models import Assessment
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from utils.django_forms import add_attr
from .forms import AssessmentForm

# Create your views here.
def assessment_view(request):
    registers = Assessment.objects.all().order_by('name')

    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)
    
    return render(request,'assessment/pages/assessment_view.html', {
        'registers': objs_per_page,
        'form_action_search': reverse('assessment:search'),
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    registers = Assessment.objects.filter(
        Q(
            Q(name__name__icontains=search_term) # "OR" in database
        ),
    ).order_by('name')

    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'assessment/pages/assessment_view.html', {
        'registers': objs_per_page,
    })

def add_view(request):
    register_form_data = request.session.pop('register_form_data', None)
    form = AssessmentForm(register_form_data)

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Avaliação',
            'form_action': reverse('assessment:add_create'),
        })

def add_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = AssessmentForm(POST)

    if form.is_valid():
        assessment = form.save(commit=False)
        assessment.save()

        messages.success(request, 'A avaliação foi salva.')

        del(request.session['register_form_data'])
        return redirect(reverse('assessment:add_view'))
    
    return redirect('assessment:add_view')

def to_view(request, id):
    enrollment = Assessment.objects.filter(
        pk=id
    ).order_by('name').first()

    form = AssessmentForm(instance=enrollment)

    for field_name, field in form.fields.items():
        field.widget.attrs['disabled']=True
        add_attr(form.fields[field_name], 'class', 'disabled') 

    return render(
        request, 'users/pages/register_view.html', {
            'form': form,
            'title': 'Informações da Avaliação',
            'enrollment': enrollment
    })