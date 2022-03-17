from tokenize import Number
from django.db import models


class Common_Problems(models.Model):
    Compliant_Type = models.CharField(max_length=600)

    def __str__(self):
        return self.Compliant_Type

class PlantModel(models.Model):
    planttype = models.CharField(max_length=60)

    def __str__(self): 
        return self.planttype
class Client(models.Model):

    FirstName = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Location  = models.CharField(max_length=200)
    plant_type_owned = models.ForeignKey(PlantModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.FirstName 
class Plant_Details(models.Model):
    plantname = models.CharField(max_length=200)
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Typeofplant = models.ForeignKey(PlantModel,on_delete=models.CASCADE)
    Delivered_on = models.DateTimeField(auto_now_add=False)
    Location = models.CharField(max_length=300)
    sample_dwarings = models.FileField()

    def __str__(self):
        return self.plantname


class created_blocks(models.Model):
    block = models.IntegerField()
    plant_name = models.ForeignKey(Plant_Details,on_delete=models.CASCADE)
       
class Compliants(models.Model):
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant_Details,on_delete=models.CASCADE)
    Compliant_type = models.ForeignKey(Common_Problems,on_delete=models.CASCADE)
    Problem_Description = models.TextField(max_length=3000)

    def __str__(self):
        return self.Problem_Description

