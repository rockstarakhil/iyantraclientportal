from django.forms import models, widgets
from import_export import resources , fields
from import_export.widgets import ForeignKeyWidget
from DataCollection.models import Client , Plant_Details

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        widget = ForeignKeyWidget(Plant_Details,'plantname')
    
