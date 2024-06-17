from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from commondatab.models import ZzFriendship, ZzUsers, ZzDiscussions, ZzUsersDiscussions
from django.contrib.auth import get_user_model
import requests



def messagerie(request):
    return render(request, 'messagerie/messagerie.html')
    #----------------------------------------------------API Endpoints---------------------------------------------------

class LikeViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        liker = request.user
        liked_id = request.data.get('liked_id')
        liked = get_user_model().objects.get(id=liked_id)
        
        ZzFriendship.objects.create(liker=liker, liked=liked, lik=1)
        if ZzFriendship.objects.filter(liker=liked, liked=liker, lik=1).exists():
            room_name = (
                f'room_{liker.id}_{liked.id}' if liker.id > liked.id else f'room_{liked.id}_{liker.id}'
            )
            discussion = ZzDiscussions.objects.get_or_create(room_name=room_name)
            if created:
                ZzUsersDiscussions.objects.create(user=liker, discussion=discussion, status=1)
                ZzUsersDiscussions.objects.create(user=liked, discussion=discussion, status=1)
        return Response(status=status.HTTP_201_CREATED)