from django.shortcuts import render, redirect
from django.http import HttpResponse
from enrollment.models import Registration
from django.core.paginator import Paginator

# Create your views here.
def enrollment_view(request):
    registers = Registration.objects.all()

    paginator = Paginator(registers, 10)
    page = request.GET.get('page')
    objs_per_page = paginator.get_page(page)

    return render(request,'enrollment/pages/enrollment_view.html', {
        'registers': objs_per_page
    })