from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def enrollment_view(request):
    return render(
        request,
        'enrollment/pages/enrollment_view.html'
    )
    return HttpResponse('Hello Enrollment')