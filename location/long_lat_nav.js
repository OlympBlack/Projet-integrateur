// Dans votre fichier JavaScript côté client
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
        // Récupérer le token CSRF depuis le cookie csrftoken 
        const csrftoken = document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];
      // Envoyez ces informations à votre serveur Django via une requête AJAX ou Fetch API
        fetch('/api/location', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken // Assurez-vous d'inclure le token CSRF de Django
            },
            body: JSON.stringify({ latitude, longitude })
        })
        .then(response => response.json())
        .then(data => {
        // Traitez les données reçues du serveur ici
            console.log(data); // par exemple, afficher les infos des users suggérés
        });
    }, function(error) {
      // Gérez les erreurs ici
        console.error("Erreur de géolocalisation : ", error);
        // Afficher un message d'erreur
        alert("Veuillez activer la geolocalisation dans votre navigateur ou saisir votre emplacement manuellement");
    });
} else {
    console.error("La géolocalisation n'est pas prise en charge par ce navigateur. Veuillez le mettre à jour ou saisir manuellement votre emplacement.");
}
