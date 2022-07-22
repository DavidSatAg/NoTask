from django.shortcuts import render

from .models import Note

def editor(request):
    noteid = int(request.GET.get('noteid , 0'))
    notes = Note.objects.all()
    context = {
        'noteid': noteid,
        'notes':notes,
    }
    return render(request, 'editor.html', context)