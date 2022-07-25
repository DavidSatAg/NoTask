from django.shortcuts import render, redirect

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

            return redirect('/?noteid=%i' % noteid)
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
    return render(request, 'editor.html', context)

def delete_note(request, noteid):
    note = Note.objects.get(pk=noteid)
    note.delete = ()

    return redirect('/?noteid=0')

