from django.urls import path
from . import views
from .views import editor, delete_note, show
urlpatterns = [
    path('', editor, name='editor' ),
    path('delete_note/<int:noteid>/', delete_note, name='delete_note'),
    path('show/', show, name='show')
]