
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    
    path(r'BarGraph',views.BarGraph),
    #path(r'graph/',views.graph),
    path(r'',views.homepage)
]
