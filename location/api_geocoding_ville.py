import requests

def obtenir_coordonnees_depuis_ville(ville):
    # Remplacez 'VOTRE_CLE_API' par votre clé API réelle obtenue de Google
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={ville}&key=VOTRE_CLE_API"
    
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        if results:
            latitude = results[0]['geometry']['location']['lat']
            longitude = results[0]['geometry']['location']['lng']
            return latitude, longitude
    return None, None

# Exemple d'utilisation
ville = "Paris"
latitude, longitude = obtenir_coordonnees_depuis_ville(ville)
if latitude and longitude:
    print(f"Les coordonnées de {ville} sont Latitude: {latitude}, Longitude: {longitude}")
