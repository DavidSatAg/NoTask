from django.urls import path
from note.views import editor
from . import views

urlpatterns = [
    # path('', views.note, name='note'),
    path('', editor, name='editor' ),
]