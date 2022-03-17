from glob import glob
from django.shortcuts import render
from . models import * 


def home(request):
    clients = Client.objects.all()
    client_counts = clients.count()
    plant_details = Plant_Details.objects.all()
    plantmodels = PlantModel.objects.all()
    compliants = Compliants.objects.all()
    compliants_counts = compliants.count()
    blocks = created_blocks.objects.all()
    no_of_blocks = blocks.count()
       
    context = {'clients':clients,'plant_details':plant_details,
    'plantmodels':plantmodels,
    'client_counts':client_counts,'compliants':compliants,
    'compliants_counts':compliants_counts,
    'blocks':blocks,'no_of_blocks':no_of_blocks}


    return render(request,'DataCollection/Home.html',context)

def about(request):
    return render(request,'DataCollection/about.html')

def user(request):
    return render(request,'DataCollection/user.html')
