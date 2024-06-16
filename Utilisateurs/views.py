from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from commondatab.models import ZzUsers
#from django.contrib.auth.decorators import login_required
'''from .forms import CompteUtilisateur'''
from django.contrib import messages

def Index(request):
    return render(request, "Utilisateurs/index.html")


def Inscription(request):
    if request.method=='POST':
        pseudo=request.POST['pseudo']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Les mots de passes ne correspondent pas')
            #return render(request, "Utilisateurs/inscription.html")
        
        if ZzUsers.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
            #return render(request, "Utilisateurs/inscription.html")
        
        user=ZzUsers.objects.create_user(pseudo=pseudo, email=email, password=password1)
        user.save()
        return redirect('Utilisateurs:index')
    
    return render(request, 'Utilisateurs/inscription.html')


def Connexion(request):
    
    return render(request, 'Utilisateurs/connexion.html')

def Profil(request):
    return render(request, 'Utilisateurs/profil.html')
