from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def login(request):
    return render(request, 'home/login.html')

def home(request):
    return render(request, 'home/index.html')

def task(request):
    return render(request, '/home/davidaguina/Workspace/NoTask/note/templates/note/index.html')