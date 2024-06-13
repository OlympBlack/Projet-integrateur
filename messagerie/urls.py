from django.urls import path
from . import views
app_name = 'messagerie'
urlpatterns = [
    path('', views.messagerie, name='messagerieInterface'),
]
    