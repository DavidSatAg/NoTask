from django.shortcuts import render

from django.http import HttpResponse
from .models import Document

# Create your views here.

# def note(request):
#     return render(request, "note/index.html")

def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents
    }

    return render(request, 'note/editor.html', context)