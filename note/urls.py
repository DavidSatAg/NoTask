from django.urls import path
from .views import AnotacaoList 
from . import views

urlpatterns = [
    # path('', views.note, name='note'),
    path('', AnotacaoList.as_view(), name='anotacoes'),
    path('post/new/', views.post_new, name='post_new')
]