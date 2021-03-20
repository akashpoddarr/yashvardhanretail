from django.shortcuts import render

# Create your views here.

def aboutpage(request):
    return render(request, 'aboutus.html')