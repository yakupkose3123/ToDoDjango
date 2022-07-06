
from django.urls import path
from .views import  home, todo_delete, todo_list, todo_create,  HomeView, TodoListView , TodoCreateView , TodoDetailView , TodoUpdateView , TodoDeleteView,  todo_update

urlpatterns = [
   #! CLASS BASED VIEWS
   # path('', HomeView.as_view(),  name="home"),
   # path('list/', TodoListView.as_view(), name="list"),
   # path('add/', TodoCreateView.as_view(), name="add"),
   # path('update/<int:pk>/', TodoUpdateView.as_view(), name="update"),
   # path('delete/<int:pk>/', TodoDeleteView.as_view(), name="delete"),

   #! FUNCTİONAL BASED VIEWS
   path('', home,  name="home"),
   path('list/', todo_list,  name="list"),   
   path('add/', todo_create, name="add"), 
   path('detail/<int:id>/', TodoDetailView.as_view(), name="detail"),  
   path('update/<int:id>/', todo_update, name="update"),   
   path('delete/<int:id>/', todo_delete, name="delete"),
]