from django.shortcuts import render
from .models import contactus
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


# Create your views here.

def contactpage(request):
    if request.method=='POST':
        contact= contactus()
        name = request.POST['fullname']
        address = request.POST['emailaddress']
        number = request.POST['primary_no']
        comment = request.POST['comments']
        contact.full_name = name
        contact.full_address = address
        contact.full_number = number
        contact.full_comment = comment
        contact.save()
        messages.success(request, 'Your From has been submitted, We will try to contact you as soon as possible !')

    return render(request, 'contactus.html')