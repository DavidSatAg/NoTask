from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Anotacao


# Create your views here.

# def note(request):
#     return render(request, "note/index.html")

class AnotacaoList(ListView):
    model = Anotacao
    context_object_name = 'anotacoes'
    
class AnotacaoDetail(DetailView):
    model = Anotacao
    context_object_name = 'anotacao'
    template_name = 'note/editor.html'

