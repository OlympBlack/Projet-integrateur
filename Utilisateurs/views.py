from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    context = {
        "message": "Hello Word !"
    }
    return render(request, "Utilisateurs/accueil.html", context)
