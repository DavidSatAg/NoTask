from django.urls import path
from note.views import editor
urlpatterns = [
    path('', editor, name='editor' )
]