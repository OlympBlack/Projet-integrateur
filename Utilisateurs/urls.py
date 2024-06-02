from django.urls import path
from . import views


app_name = "Utilisateurs"
urlpatterns = [
    path('', views.index, name='index')
]