import re
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'DataCollection/home.html')

#def about(request):
 #   return render(request,'DataCollection/about.html')
