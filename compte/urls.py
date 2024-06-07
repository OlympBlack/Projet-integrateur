from django.urls import path
from . import views

urlpatterns = [
    path('/inscription', views.InscriptionPage, name='inscription'),
    path('', views.ConnexionPage, name='connexion'),
]
