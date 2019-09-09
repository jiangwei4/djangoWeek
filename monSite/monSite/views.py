# monSite/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse('Hello world')

def home_page_view_with_render(request):
    return render(request,'home_page.html')

def form(request):
    if request.method == "POST":
        print(request.POST)
        alpha = request.POST["data"]
        print(alpha)
    return render(request, "form_page.html",{"value1":alpha})