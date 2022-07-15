from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Anotacao


# Create your views here.

# def note(request):
#     return render(request, "note/index.html")

class AnotacaoList(ListView):
    model = Anotacao
    context_object_name = 'anotacoes'
    template_name = 'note/editor.html'
