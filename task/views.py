from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa
# Create your views here.
class TarefaList(ListView):
    model = Tarefa
    context_object_name= 'tarefas'
    template_name = 'task/tarefa_list.html'
class TarefaDetail(DetailView):
    model = Tarefa
    context_object_name= 'tarefa'
    template_name = 'task/tarefa.html'
class TarefaCreate(CreateView):
    model = Tarefa
    fields = '__all__'
    success_url= reverse_lazy('tarefas')
class TarefaUpdate(UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url= reverse_lazy('tarefas')
class DeleteView(DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url= reverse_lazy('tarefas')