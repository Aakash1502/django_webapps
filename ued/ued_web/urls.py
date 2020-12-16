from django.contrib import admin
from django.urls import path, include
from ued_web import views

urlpatterns = [ 
   path('', views.home, name='home'),
   path('ux/',views.ux, name='ux'),
   path('art/',views.art, name='art')
]