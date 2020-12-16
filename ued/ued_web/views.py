from django.shortcuts import render,HttpResponse
from ued_web.models import uxwork,artwork
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def ux(request):
    allPosts = uxwork.objects.all() 
    context = {'allPosts': allPosts}
    return render(request,'home/ux.html', context)

def art(request):
    artPosts = artwork.objects.all() 
    context1 = {'artPosts': artPosts}
    return render(request,'home/art.html', context1)
    