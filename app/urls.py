
from django.urls import path
from django.views.generic.base import TemplateView
from .views import  HomeView, TodoListView , TodoCreateView , TodoDetailView , TodoUpdateView , TodoDeleteView

urlpatterns = [
   path('', HomeView.as_view(),  name="home"),

   path('list/', TodoListView.as_view(), name="list"),

   path('add/', TodoCreateView.as_view(), name="add"), 

   path('detail/<int:id>/', TodoDetailView.as_view(), name="detail"), 

   path('update/<int:pk>/', TodoUpdateView.as_view(), name="update"),

   path('delete/<int:pk>/', TodoDeleteView.as_view(), name="delete"),
]