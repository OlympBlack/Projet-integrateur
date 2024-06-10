from django.shortcuts import render
from django.http import HttpResponse
'''from .forms import CompteUtilisateur
from django.contrib import messages'''

#la fonction qui retourne la page index
def Index(request):
    return render(request, "Utilisateurs/index.html")

#la fonction pour la la page d'inscription
def Inscription(request):
    return render(request, 'Utilisateurs/inscription.html')


#la fonction pour la la page d'inscription
def Connexion(request):
    return render(request, 'Utilisateurs/connexion.html')
