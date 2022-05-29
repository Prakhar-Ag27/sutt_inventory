from django.shortcuts import render
from .models import items
from django.http import HttpResponse
from django.shortcuts import render


def details(request):
    item_list = items.objects.all()[:]
    context = {'item_list': item_list}
    if request.user.is_authenticated:
        return render(request, 'fnapp/detailspage.html', context)
        
    else:
        return render(request, 'fnapp/notlogin.html')

def issue(request):
    if request.user.is_authenticated:
        return render(request, 'fnapp/issuepage.html')
    else:
        return render(request, 'fnapp/notlogin.html')