from django.shortcuts import render
from .models import items
from django.http import HttpResponse
from django.shortcuts import render

def details(request):
    return render(request, 'fnapp/detailspage.html')

def issue(request):
    return render(request, 'fnapp/issuepage.html')