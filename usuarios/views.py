from django.shortcuts import render
from django.http import HttpResponse

def register_view(request):
    return HttpResponse('Register View')