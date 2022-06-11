from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ToDoForm
from .models import Todo

from app.models import Todo

#!HOME
def home(request) :
    return render(request, "app/home.html")
class HomeView(TemplateView):
    template_name = "app/home.html" 

#!LİST
def todo_list(request) : 
    todos = Todo.objects.all()
    context = {"todos" : todos}

    return render(request, "app/todo_list.html", context)


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'

#!ADD

def todo_create(request):
    form = ToDoForm()

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = { "form" : form}
    return render(request, "app/todo_add.html", context)

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
def todo_update(request, id):
    todo = Todo.objects.get(id=id)    
    form = ToDoForm(instance=todo)

    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = { 
        "todo" : todo,
        "form" : form
        }

    return render(request, "app/todo_update.html", context)
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = ToDoForm 
    template_name = "app/todo_update.html"
    success_url = reverse_lazy('list')

#! DELETE 

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        todo.delete()
        return redirect("list") 
    context = {"todo" : todo}   

    return render(request, "app/todo_delete.html", context)

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "app/todo_delete.html"
    success_url = reverse_lazy('list')
    