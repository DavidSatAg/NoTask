from django.urls import path
from .views import AnotacaoList

urlpatterns = [
    # path('', views.note, name='note'),
    path('', AnotacaoList.as_view(), name='anotacoes')
]