from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ToDoForm

from app.models import Todo


class HomeView(TemplateView):
    template_name = "app/home.html" 

#!LİST
class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'

#!ADD

class TodoCreateView(CreateView):
    model = Todo
    form_class = ToDoForm   
    template_name = "app/todo_add.html"    
    success_url = reverse_lazy("list")

#!DETAİL
class TodoDetailView(DetailView):
    model = Todo
    pk_url_kwarg = 'id'

#!UPDATE

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = ToDoForm 
    template_name = "app/todo_update.html"
    success_url = reverse_lazy('list')

#! DELETE 

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "app/todo_delete.html"
    success_url = reverse_lazy('list')
    