from django.shortcuts import render, redirect, get_object_or_404

from .models import Note

def editor(request):
    noteid = int(request.GET.get('noteid' , 0))
    notes = Note.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title', 0)
        content = request.POST.get('content', '')
        if noteid > 0:
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()

            return redirect('editor')
        else:
            note = Note.objects.create(title= title, content=content)

            return redirect('/?noteid=%i' % note.id)
    
    
    if noteid > 0:
        note = Note.objects.get(pk=noteid)
    else:
        note = ''


    context = {
        'noteid': noteid,
        'notes':notes,
        'note': note,
    }
    return render(request, 'note/editor.html', context)

def delete_note(request, noteid):
    note = get_object_or_404(Note, id=noteid)
    note.delete()
    # return render(request, 'note/show.html', note)
    return redirect('editor')

def show(request):
    notas = Note.objects.all()
    context= {
        'notas': notas
    }
    return render(request, 'note/show.html', context)