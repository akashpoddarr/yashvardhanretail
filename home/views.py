from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    # print(request.session.get('email'))      know about the user if is registered or not 
    return render(request, 'index.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('/')

