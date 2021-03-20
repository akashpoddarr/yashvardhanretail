from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileModelForm
from django.views.generic import DetailView
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string




# Create your views here.

# userpanel page function
def userpanel(request):
    return render(request, 'userpanel.html')

# signup function


def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for anny error
        if pass1 != pass2:
            messages.error(request, 'your passwords do not match')
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username=username, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        template = render_to_string('email_template.html')
        email = EmailMessage(
            'Thank you for registering at YashvardhanRetail.com !!',
            template,
            settings.EMAIL_HOST_USER,
            [myuser.username],
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'your account has been created successfully')
        return redirect('/')

    else:
        return HttpResponse("404 not found")

# login function


def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            # session
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            # session code ends
            login(request, user)
            messages.success(request, 'Successfully Logged In!!!')
            return redirect('/')
        else:
            messages.error(
                request, 'You Have Entered Invalid Credentials, Please Try Again!!!')

        return redirect('/')
    return HttpResponse("404 not found")


# logout function
def handlelogout(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('/')


# # my profile page function
# @login_required
# def myprofile(request):
#     profile = Profile.objects.get(user=request.user)
#     form = ProfileModelForm(request.POST or None, request.Files or None, instance=profile)
#     confirm = False

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             confirm = True

#     context = {
#         'profile': profile,
#         'form': form,
#         'confirm': confirm,
#     }


#     return render(request,'myprofile.html', context)

@login_required
def myprofile(request):

    if request.user.is_authenticated:
        context = {
            'user': request.user,

        }
        return render(request, 'myprofile.html', context)
    
        

@login_required
def myprofilesettings(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form, 
        'confirm': confirm,
    }
    return render(request, 'myprofilesettings.html', context)
