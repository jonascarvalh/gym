from django.shortcuts import render
from django.http import HttpResponse

def register_view(request):
    return render(request, 'usuarios/pages/register_view.html')
