import json
import math

def calculer_distance_haversine(lat1, lon1, lat2, lon2):
    # Convertir les latitudes et longitudes de degrés en radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Formule de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Rayon de la Terre en kilomètres (vous pouvez changer cela pour des miles)
    rayon_terre = 6371

    # Calculer la distance
    distance = rayon_terre * c

    return distance

# Exemple d'utilisation
lat1 = 48.8566  # Latitude de Paris
lon1 = 2.3522   # Longitude de Paris
lat2 = 40.7128  # Latitude de New York
lon2 = -74.0060 # Longitude de New York

distance = calculer_distance_haversine(lat1, lon1, lat2, lon2)
print(f"La distance entre Paris et New York est de {distance} kilomètres.")


donnees_json = '{"user1": {"latitude": 48.8566, "longitude": 2.3522}, "user2": {"latitude": 40.7128, "longitude": -74.0060}}'

# Parser le JSON pour obtenir un dictionnaire Python
coordonnees = json.loads(donnees_json)

# Extraire les coordonnées des utilisateurs
lat1 = coordonnees['user1']['latitude']
lon1 = coordonnees['user1']['longitude']
lat2 = coordonnees['user2']['latitude']
lon2 = coordonnees['user2']['longitude']

# Calculer la distance entre les deux utilisateurs
distance = calculer_distance_haversine(lat1, lon1, lat2, lon2)
print(f"La distance entre les deux utilisateurs est de {distance} kilomètres.")