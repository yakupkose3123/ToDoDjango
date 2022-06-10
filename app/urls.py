
from django.urls import path
from django.views.generic.base import TemplateView
from .views import  HomeView

urlpatterns = [
   path('', HomeView.as_view(),  name="home"),   
    
    
]