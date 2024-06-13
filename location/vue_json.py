# Dans votre vue Django
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST"])
def location_view(request):
    data = json.loads(request.body)
    latitude = data['latitude']
    longitude = data['longitude']

    # Utilisez ces informations pour filtrer les utilisateurs par distance
    # ...

    return JsonResponse({'status': 'success', 'data': filtered_users})
