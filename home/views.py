from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home/index.html')
def task(request):
    return render(request, '/home/davidaguina/Workspace/NoTask/note/templates/note/index.html')