from os import abort
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home)
]
