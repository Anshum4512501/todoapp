
from django.urls import path
from .views import SignUpView,HomeView,LoginView, ToDoCompletedTasksListView,ToDoCreateView,ToDoCurrentTaskListView,ToDoDetailView,ToDoDeleteView,ToDoUpdateView,complete_date
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('signup/',SignUpView.as_view(),name="signup"),
    path('',HomeView.as_view(),name="home"),
    path('signin/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('newtask/',ToDoCreateView.as_view(),name="newtask"),
    path('alltask/',ToDoCurrentTaskListView.as_view(),name="currenttasks"),
    
    path('task/',ToDoCompletedTasksListView.as_view(),name="completedtasks"),
    
    path('task/<slug:pk>',ToDoDetailView.as_view(),name="detail"),
    path('task/<slug:pk>/delete',ToDoDeleteView.as_view(),name="delete"),
    path('task/<slug:pk>/update',ToDoUpdateView.as_view(),name="update"),
    path('task/<slug:pk>/complete',complete_date,name="complete"),
    # path('task/<slug:pk>/',NotesCreateView.as_view(),name="notes_create"),
]