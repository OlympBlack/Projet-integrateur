from django.shortcuts import render
from django.http import HttpResponse
'''from .forms import CompteUtilisateur
from django.contrib import messages'''

#la fonction qui retourne la page index
def index(request):
    return render(request, "Utilisateurs/index.html")

#la fonction pour la validation du formulaire
'''def InscriptionPage(request):
    form = CompteUtilisateur()
    if request.methd == 'post':
        form = CompteUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'Utilisateur/index', context)'''

