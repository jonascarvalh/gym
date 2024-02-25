from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from assessment.models import Assessment
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from utils.django_forms import add_attr

# Create your views here.
def assessment_view(request):
    registers = Assessment.objects.all().order_by('name')

    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)
    
    return render(request,'assessment/pages/assessments_view.html', {
        'registers': objs_per_page,
        'form_action_search': reverse('assessment:search'),
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    registers = Assessment.objects.filter(
        Q(
            Q(name__icontains=search_term) | # "OR" in database
            Q(sig_register__icontains=search_term),
        ),
    ).order_by('name')


    paginator = Paginator(registers, 8)
    page      = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'assessment/pages/assessment_view.html', {
        'registers': objs_per_page,
    })