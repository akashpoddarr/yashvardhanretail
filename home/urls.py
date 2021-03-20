from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name ="homepage"),
	path('logout/', views.handlelogout, name="handlelogout"),

    

]
