from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def note(request):
    return render(request, "note/index.html")