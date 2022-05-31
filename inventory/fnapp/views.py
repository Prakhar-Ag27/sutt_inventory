from imp import reload
from django.shortcuts import render
from .models import Item, Through, Student
from django.http import HttpResponse
from django.shortcuts import render
import smtplib
import os

def details(request):
    try:
        obj = Student.objects.get(email_id = request.user.email)
    except Student.DoesNotExist:
        obj = Student(first_name=request.user.first_name, last_name=request.user.last_name, email_id=request.user.email)
        obj.save()

    item_list = Item.objects.all()
    context = {'item_list': item_list}
    if request.user.is_authenticated:
        return render(request, 'fnapp/detailspage.html', context)
        
    else:
        return render(request, 'fnapp/notlogin.html')

def issue(request, itemcode):
    tobeissued = Item.objects.get(unique_code=itemcode)
    context = {'tobeissued': tobeissued}
    if request.user.is_authenticated:
        return render(request, 'fnapp/issuepage.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')

def success(request, itemcode):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            pass
        else:
            obj = Through()
            obj.item = Item.objects.get(unique_code=itemcode)
            obj.student = Student.objects.get(email_id=request.user.email)
            obj.qty_issued = int(request.POST['items'])
            obj.save()
        print(int(request.POST['items']))
        item_issued = Item.objects.get(unique_code = itemcode)
        item_issued.total_qty = item_issued.total_qty - int(request.POST['items'])
        item_issued.current_out = item_issued.current_out + int(request.POST['items'])
        item_issued.save()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("agrawal.prakhar35@gmail.com", "tndumdixwmkppymx")
            subject = 'Regarding issue of item from IMS'
            body = f'You have successfully issued {Item.name_of_item} with item code {Item.unique_code}.'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("agrawal.prakhar35@gmail.com", request.user.email, msg)

        return render(request, 'fnapp/successpage.html', {"itemcode" : itemcode})

    else:
        return render(request, 'fnapp/notlogin.html')

def log_add(request):
    logitems = Item.objects.all().order_by(-'added_on')
    context = {'logitems': logitems}
    if request.user.is_authenticated:
        return render(request, 'fnapp/log_add.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')

def log_issue(request):
    logitems = Through.objects.all().order_by(-'time_of_issue')
    context = {'logitems': logitems}
    if request.user.is_authenticated:
        return render(request, 'fnapp/log_issue.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')

def log_return(request):
    logitems = Through.objects.all().order_by(-'time_of_return')
    context = {'logitems': logitems}
    if request.user.is_authenticated:
        return render(request, 'fnapp/log_return.html', context)
    else:
        return render(request, 'fnapp/notlogin.html')
    

