from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html')

@login_required
def private_page(request):
    return render(request, 'seven_ch/index.html', {})

def public_page(request):
    return render(request, 'blog/index.html', {})