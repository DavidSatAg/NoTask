from django.shortcuts import render

from .models import Note

def editor(request):
    noteid = int(request.GET.get('noteid' , 0))
    notes = Note.objects.all()

    if noteid > 0:
        note = Note.objects.get(pk=noteid)
    else:
        note = ''

    context = {
        'noteid': noteid,
        'notes':notes,
        'note': note,
    }
    return render(request, 'editor.html', context)

