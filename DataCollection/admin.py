from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from DataCollection.models import Client , Plant_Details , PlantModel , Common_Problems ,Compliants,created_blocks    

#admin.site.register(Client)
admin.site.register(Plant_Details)
admin.site.register(PlantModel)
admin.site.register(Common_Problems)
admin.site.register(Compliants)
admin.site.register(created_blocks)

@admin.register(Client)
class CustomerResource(ImportExportModelAdmin):
    list_display = ("FirstName","Last_Name","Location")
    encoding="utf8",
    pass