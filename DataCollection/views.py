import re
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome To Iyantra Client Portal<h1>")

#def about(request):
 #   return render(request,'DataCollection/about.html')
