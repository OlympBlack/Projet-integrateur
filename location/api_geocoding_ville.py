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
