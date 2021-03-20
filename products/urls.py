from django.contrib import admin
from django.urls import path
from . import views
from . views import ProductD

urlpatterns = [
    path('', ProductD.as_view(),name ="productsmainpage"),
    path('detail/<int:pk>', views.detail,name='detail'),
    

]
