// Script JavaScript pour traiter la soumission du formulaire
document.getElementById('locationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ville = document.getElementById('cityInput').value;

    // Remplacez 'VOTRE_CLE_API' par votre clé API réelle obtenue de Google
    const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${ville}&key=VOTRE_CLE_API`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'OK') {
                const latitude = data.results[0].geometry.location.lat;
                const longitude = data.results[0].geometry.location.lng;
                // Utilisez les coordonnées comme nécessaire
                console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
            } else {
                // Gérez le cas où la ville n'est pas trouvée
                console.error('Ville non trouvée');
            }
        })
        .catch(error => {
            // Gérez les erreurs de réseau ou autres erreurs
            console.error('Erreur lors de la requête de géocodage:', error);
        });
});