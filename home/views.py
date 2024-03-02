from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    return render(request, 'home/pages/home.html', {
        'request': request
    })