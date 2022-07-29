from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TarefaList(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name= 'tarefas'
    template_name = 'task/tarefa_list.html'
class TarefaDetail(LoginRequiredMixin, DetailView):
    model = Tarefa
    context_object_name= 'tarefa'
    template_name = 'task/tarefa.html'
class TarefaCreate(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = '__all__'
    success_url= reverse_lazy('tarefas')
class TarefaUpdate(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url= reverse_lazy('tarefas')
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url= reverse_lazy('tarefas')