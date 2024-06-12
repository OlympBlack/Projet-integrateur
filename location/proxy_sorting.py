import calculer_distance_haversine  # Importer la fonction calculer_distance_haversine
# Fonction pour filtrer les utilisateurs par proximité
def filtrer_utilisateurs_proximite(utilisateur_actuel, rayon):
    utilisateurs_proches = []
    for utilisateur in liste_utilisateurs:
        distance = calculer_distance_haversine(
            utilisateur_actuel['latitude'],
            utilisateur_actuel['longitude'],
            utilisateur['latitude'],
            utilisateur['longitude']
        )
        if distance <= rayon:
            utilisateurs_proches.append(utilisateur)
    
    # Appliquer d'autres critères de filtrage si nécessaire
    # ...

    # Trier les utilisateurs par distance croissante
    utilisateurs_proches.sort(key=lambda x: x['distance'])

    return utilisateurs_proches

# Exemple d'utilisation
utilisateur_actuel = {'latitude': 48.8566, 'longitude': 2.3522}  # Coordonnées de Paris
rayon_recherche = 20  # Rayon de recherche en kilomètres
resultats = filtrer_utilisateurs_proximite(utilisateur_actuel, rayon_recherche)
