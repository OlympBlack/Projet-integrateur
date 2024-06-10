from django.db import models

#La table des Utilisateurs 
class Zz_Users(models.Model):
    zz_email = models.EmailField(unique=True, max_length=100)
    zz_password = models.CharField(max_length=100)


class Zz_MediaFile(models.Model):
    zz_user = models.ForeignKey(Zz_Users, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media_files/')
    # la table des médias ou vidéos...

    




class Zz_profile(models.Model):
    zz_user = models.OneToOneField(Zz_Users, on_delete=models.CASCADE)
    zz_name = models.CharField(unique=True, max_length=100)
    zz_prenom =models.CharField(max_length=100)

    zz_date_naissance = models.DateField(unique=False)
    
    zz_sexe = models.CharField(max_length=255, choices=[('M', 'Masculin'), ('F', 'Féminin')], unique=False)
    
    zz_recherche = models.CharField(max_length=255, choices=[(0, 'homme'), (1, 'Femme'), (None, 'les deux')], unique=False)
    
    zz_profile_picture = models.ImageField(upload_to='profile_pics/')
    
    zz_additional_media = models.ManyToManyField(Zz_MediaFile, blank=True)

