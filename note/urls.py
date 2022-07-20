from django.urls import path
from .views import AnotacaoList 
from . import views

urlpatterns = [
    # path('', views.note, name='note'),
    path('post/new/', views.post_new, name='anotacoes'),
    path('', AnotacaoList.as_view(),  name='post_new')
]