from os import abort
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='portal-home'),
    path("about/", views.about)
]
