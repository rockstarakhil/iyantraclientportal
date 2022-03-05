from django.shortcuts import render
from . models import *


def home(request):
    clients = Client.objects.all()
    return render(request,'DataCollection/Home.html',{'clients':clients})

def about(request):
    return render(request,'DataCollection/about.html')
