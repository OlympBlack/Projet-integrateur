from django.urls import path
from . import views


app_name = "Utilisateurs"
urlpatterns = [
    path('Acceuil/', views.accueil, name='accueil')
]