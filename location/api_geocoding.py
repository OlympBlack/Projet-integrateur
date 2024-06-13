"""import requests

def obtenir_adresse(lat, lon):
    # Remplacez 'VOTRE_CLE_API' par votre clé API réelle obtenue du service de géocodage
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key=CLE_API_GUERIN"
    
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        if results:
            adresse_complete = results[0]['formatted_address']
            elements_adresse = results[0]['address_components']
            ville = None
            pays = None
            for element in elements_adresse:
                if 'locality' in element['types']:
                    ville = element['long_name']
                elif 'country' in element['types']:
                    pays = element['long_name']
            return ville, pays
    return None, None

# Exemple d'utilisation
latitude = 48.8566  # Latitude de Paris
longitude = 2.3522  # Longitude de Paris
ville, pays = obtenir_adresse(latitude, longitude)
print(f"Ville: {ville}, Pays: {pays}")"""


import requests

def get_location_info(latitude, longitude):
    access_token = 'VOTRE_MAPBOX_ACCESS_TOKEN'
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{longitude},{latitude}.json?access_token={access_token}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extrait la ville et le pays depuis les données
        city = data['features'][0]['text']
        country = data['features'][0]['context'][-1]['text']
        return city, country
    else:
        return None, None


