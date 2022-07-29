from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('login/', CustomLoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]