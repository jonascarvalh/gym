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
        request, 'assessment/pages/to_view.html', {
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
    assessment = Assessment.objects.filter(
        pk=id
    ).order_by('name').first()

    form = AssessmentForm(instance=assessment)

    for field_name, field in form.fields.items():
        field.widget.attrs['disabled']=True
        add_attr(form.fields[field_name], 'class', 'disabled') 

    return render(
        request, 'assessment/pages/to_view.html', {
            'form': form,
            'title': 'Informações da Avaliação',
            'enrollment': assessment
    })

def to_edit(request, id):
    assessment = get_object_or_404(Assessment, pk=id)
    
    register_form_data = request.session.pop('register_form_data', None)
    form = AssessmentForm(register_form_data, instance=assessment)
    
    url_parameter = reverse('assessment:edit_create', kwargs={'id': assessment.id})
    return render(
        request, 'assessment/pages/to_view.html', {
            'form': form,
            'title': 'Atualizar Avaliação',
            'enrollment': assessment,
            'form_action': url_parameter,
    })
    
def edit_create(request, id):
    if not request.POST:
        raise Http404()
    
    assessment = get_object_or_404(Assessment, pk=id)
    form = AssessmentForm(request.POST, instance=assessment)
    
    url_parameter = reverse('assessment:to_edit', kwargs={'id': assessment.id})
    
    if form.is_valid():
        user = form.save(commit=False)
        user.save()

        messages.success(request, 'A avaliação foi editada.')
        return redirect(url_parameter)
    
    request.session['register_form_data'] = request.POST
    return redirect(url_parameter)

def delete_create(request, id):
    # add here later: request.<is_avaliador, is_admin>
    assessment = get_object_or_404(Assessment, pk=id)
    name = assessment.name
    assessment.delete()

    messages.success(request, f'A avaliação do(a) {name} foi deletada!')
    
    return redirect(reverse('assessment:assessment_view'))