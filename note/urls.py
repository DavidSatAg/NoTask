from django.urls import path
from .views import AnotacaoCreate, AnotacaoList, AnotacaoCreate
from . import views

urlpatterns = [
    # path('', views.note, name='note'),
    path('post/new/', views.post_new, name='anotacoes'),
    path('', AnotacaoList.as_view(),  name='post_new'),
    path('note-create',AnotacaoCreate.as_view, name='note-create'),
]