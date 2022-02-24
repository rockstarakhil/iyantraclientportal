from django.contrib import admin

from DataCollection.models import Client , Plant_Details , PlantModel , Common_Problems ,Compliants

admin.site.register(Client)
admin.site.register(Plant_Details)
admin.site.register(PlantModel)
admin.site.register(Common_Problems)
admin.site.register(Compliants)
