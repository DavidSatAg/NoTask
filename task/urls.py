from django.urls import path
from .views import TarefaList, TarefaDetail, TarefaCreate, TarefaUpdate, DeleteView
urlpatterns = [
    path('', TarefaList.as_view(), name='tarefas'),
    path('tarefa/<int:pk>/', TarefaDetail.as_view(), name='tarefa'),
    path('tarefa-create/', TarefaCreate.as_view(), name='tarefa-create'),
    path('tarefa-update/<int:pk>/', TarefaUpdate.as_view(), name='tarefa-update'),
    path('tarefa-delete/<int:pk>/', DeleteView.as_view(), name='tarefa-delete'),
]