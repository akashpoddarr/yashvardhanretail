from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userpanel,name ="userpanelmainpage"),
    path('signup/', views.handlesignup, name="handlesignup"),
	path('login/', views.handlelogin, name="handlelogin"),
	path('logout/', views.handlelogout, name="handlelogout"),
	path('myprofilesettings/', views.myprofilesettings, name="profile_settings"),
	path('myprofile/', views.myprofile, name="profile"),

]
