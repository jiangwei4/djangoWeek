# monSite/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse('Hello world')

#def home_page_view_with_render(request):
 #   return render(request,'home_page.html')

def home_page_view_with_render(request):
    if request.method == "POST":
        print(request.POST)
        alpha = 'ko'
        alpha = request.POST["data"]
        print(alpha)
    return render(request, "home_page.html",{"value1":'alpha'})