from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls.base import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView,logout_then_login,LoginView
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,ListView,DeleteView,UpdateView
from .forms import ToDoForm
from .models import ToDo
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(SuccessMessageMixin,CreateView):
    form_class = UserCreationForm
    template_name = 'todoapp/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        view = super(SignUpView,self).form_valid(form)
        username,password  = form.cleaned_data['username'],form.cleaned_data['password1']
        user = authenticate(username=username,password= password)
        if user:
            login(self.request,user)
            return view
        raise ValidationError("Not valid values from ")        
        

class LoginView(SuccessMessageMixin,LoginView):
    template_name = 'todoapp/login.html'
    form_class = AuthenticationForm
    success_message = "SuccessFully Logged IN"
    

class HomeView(TemplateView,LoginRequiredMixin):
    template_name = 'todoapp/home.html'

class ToDoCreateView(LoginRequiredMixin,CreateView):
    form_class = ToDoForm
    success_url = reverse_lazy('home')
    template_name = 'todoapp/task_create.html'   
    login_url = reverse_lazy('login')
     
    def  form_valid(self, form):
        form.instance.user = self.request.user
        return  super().form_valid(form)


class ToDoCurrentTaskListView(LoginRequiredMixin,ListView):
    template_name = 'todoapp/task_list.html'   
    login_url = reverse_lazy('login')
     
    model = ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = ToDo.objects.all().filter(user=self.request.user).filter(completed_at=None)
        return context

class ToDoCompletedTasksListView(LoginRequiredMixin,ListView):
    template_name = 'todoapp/task_list.html'   
    login_url = reverse_lazy('login')
     
    model = ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = ToDo.objects.all().filter(user=self.request.user).exclude(completed_at=None)
        return context
class ToDoDetailView(LoginRequiredMixin,DetailView):
    template_name = 'todoapp/task_detail.html'   
    login_url = reverse_lazy('login')
     
    model = ToDo    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = ToDo.objects.get(id=self.kwargs['pk'])
        print("context['item']",context['item'])
        return context


class ToDoDeleteView(LoginRequiredMixin,DeleteView):
    
    template_name = 'todoapp/task_detele.html'   
    login_url = reverse_lazy('login')
    model = ToDo
    success_url = reverse_lazy('home')
            
    

class ToDoUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'todoapp/task_create.html'   
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home') 
    model = ToDo
    form_class = ToDoForm

    def form_valid(self, form) -> HttpResponse:
        form.instance.completed_at = None
        return super().form_valid(form)

def complete_date(request,pk):
    try:
      instance = ToDo.objects.get(pk=pk)
      
    except ToDo.DoesNotExist:
        raise Http404("Todo does not exist")
    if instance.completed_at is None:
        instance.complete_task()
        context = {'completed':True,'item':instance}
        return render(request,'todoapp/task_detail.html',context)
    return HttpResponse("This partucular task is already completed")    
    

