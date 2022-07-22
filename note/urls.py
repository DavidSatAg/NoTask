from django.urls import path
from . import views
from .views import editor
urlpatterns = [
    path('', editor, name='editor' )
]


