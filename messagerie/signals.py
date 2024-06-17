from django.db.models.signals import post_save
from django.dispatch import receiver
from commondatab.models import *
from django.db.models import Q

@receiver(post_save, sender=ZzFriendship)
def create_discussion_on_mutual_like(sender, instance, created, **kwargs):
    if created: 
        liker = instance.liker
        liked = instance.liked
        if ZzFriendship.objects.filter(liker=liked, liked=liker, lik=1).exists():
            room_name = (
                f'{liker.id}_{liked.id}' if liker.id > liked.id else f'{liked.id}_{liker.id}'
            )
            discussion, created = ZzDiscussions.objects.get_or_create(room_name=room_name)
            if created:
                ZzUsersDiscussions.objects.create(user=liker, discussion=discussion, status=1)
                ZzUsersDiscussions.objects.create(user=liked, discussion=discussion, status=1)