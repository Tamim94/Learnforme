from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render

from Learnforme.models import UserProfile


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['user_role'] = request.user.userprofile.role  # Use 'userprofile' instead of 'profile'
    return render(request, 'index.html', context)
def python(request):
    return render(request, 'courses/python.html')

def javascript(request):
    return render(request, 'courses/javascript.html')

def java(request):
    return render(request, 'courses/java.html')

def cpp(request):
    return render(request, 'courses/cpp.html')

def php(request):
    return render(request, 'courses/php.html')

def ruby(request):
    return render(request, 'courses/ruby.html')

def csharp(request):
    return render(request, 'courses/csharp.html')

def haskell(request):
    return render(request, 'courses/haskell.html')

# views.py
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login.html')

def createuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Le nom d\'utilisateur existe déjà.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'L\'email existe déjà.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user_profile = UserProfile(user=user, role=role)
                user_profile.save()
                messages.success(request, 'Compte créé avec succès.')

                # Authenticate and log in the user
                user = authenticate(username=username, password=password1)
                if user is not None:
                    auth_login(request, user)
                    return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
    return render(request, 'createuser.html')


def profile(request):
    return render(request, 'profile.html')


