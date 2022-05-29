from django.shortcuts import render
from .models import items, issue_items
from django.http import HttpResponse
from django.shortcuts import render
from .forms import issue_form
import django.contrib.auth


def details(request):
    item_list = items.objects.all()[:]
    context = {'item_list': item_list}
    if request.user.is_authenticated:
        return render(request, 'fnapp/detailspage.html', context)
        
    else:
        return render(request, 'fnapp/notlogin.html')

def issue(request, itemcode):
    tobeissued = items.objects.all()[:]
    context = {'tobeissued': tobeissued, "itemcode" : itemcode}
    if request.user.is_authenticated:
        return render(request, 'fnapp/issuepage.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')

def success(request, itemcode):
    if request.user.is_authenticated:
        z = items.objects.all()[:]
        
        for item_req in z:
            if item_req.unique_code == itemcode:
                obj = issue_items()
                obj.username_of_borrower = request.user.username
                obj.email_of_borrower = request.user.email
                obj.borrowed_item_code = itemcode
                obj.save()

        for item_req in z:
            if item_req.unique_code == itemcode:
                item_req.no_of_items_issued_out = item_req.no_of_items_issued_out + 1
                item_req.qty_available = item_req.qty_available - 1
                item_req.save()
        return render(request, 'fnapp/successpage.html', {"itemcode" : itemcode})
    else:
        return render(request, 'fnapp/notlogin.html')

def log_add(request):
    logitems = items.objects.all()[:]
    context = {'logitems': logitems}
    if request.user.is_authenticated:
        return render(request, 'fnapp/log_add.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')

def log_transact(request):
    logitems = issue_items.objects.all()[:]
    context = {'logitems': logitems}
    if request.user.is_authenticated:
        return render(request, 'fnapp/log_transact.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')