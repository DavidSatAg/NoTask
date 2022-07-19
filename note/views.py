from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Anotacao


# Create your views here.

# def note(request):
#     return render(request, "note/index.html")

class AnotacaoList(ListView):
    model = Anotacao
    context_object_name = 'anotacoeslist'
    template_name = 'note/editor.html'
    
class AnotacaoDetail(DetailView):
    model = Anotacao
    context_object_name = 'anotacoesdetail'
    template_name = 'note/editor.html'

class AnotacaoCreate(CreateView):
    model = Anotacao
    fields = '__all__'
    success_url = reverse_lazy('anotacoeslist')
    
class DeleteAnotacao(DeleteView):
    model = Anotacao
    context_object_name = 'anotacoesdel'
    success_url = reverse_lazy('anotacoeslist')