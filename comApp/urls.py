from django.urls import path 
from comApp import views 


urlpatterns = [
    path('',views.index,name='index')
]