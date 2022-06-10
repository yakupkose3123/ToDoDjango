from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "app/home.html" 

