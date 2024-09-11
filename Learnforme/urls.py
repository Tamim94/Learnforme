"""Learnforme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import index  # Add this line to import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Add this line to set index as the default view

    path('python/', views.python, name='python'),
    path('javascript/', views.javascript, name='javascript'),
    path('java/', views.java, name='java'),
    path('cpp/', views.cpp, name='cpp'),
    path('php/', views.php, name='php'),
    path('ruby/', views.ruby, name='ruby'),
    path('csharp/', views.csharp, name='csharp'),
    path('login/', views.login, name='login'),

    path('haskell/', views.haskell, name='haskell'),

    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('createuser/', views.createuser, name='createuser'),  # Add this line


]
