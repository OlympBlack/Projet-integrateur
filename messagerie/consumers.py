import json
from channels.db import DatabaseSyncToAsync
from channels.generic.websocket import AsyncWebsocketConsumer
from messagerie.models import Messages
from commondatab.models import *
from django.contrib.auth import get_user_model
class MessagerieConsumer(AsyncWebsocketConsumer):
    async def connect(self):
            
        if self.scope["user"].is_authenticated:
            current_user_id = self.scope['user'].id #if self.scope['user'].is_authenticated else int(self.scope['query_string'])
            other_user_id = self.scope['url_route']['kwargs']['id']
            self.room_name = (
                f'{current_user_id}_{other_user_id}' if current_user_id > other_user_id else f'{other_user_id}_{current_user_id}'
            ) 
            
            self.room_group_name = f'chat_{self.room_name}'
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            # await self.send(text_data=self.room_group_name)
        else:
            await self.close()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        #await self.disconnect(close_code)
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        content = data['content']
        user_username = data['userUsername'].replace('"', '')
        user = await self.get_user(user_username)#.replace('"', ''))
        discussion = await self.get_or_create_discussion(self.room_name)
        await self.save_message(user=user, content=content, discussion=discussion)
        messages = await self.get_messages(self.room_name) 
    
        # Envoyer le message au serveur Django
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'messagerie_message',
                'content': content,
                'userUsername': user_username,
                'messages': messages,
            },
        )

    async def messagerie_message(self, event):
        content = event['content']
        username = event['userUsername']
        messages = event['messages']
        
        
        await self.send( 
            text_data=json.dumps(
                {
                    'content': content,
                    'userUsername': username,
                    'messages': messages,
                }
            )
        )
        
        @DatabaseSyncToAsync
        def get_user(self, username):
            return get_user_model().objects.filter(username=username).first()
        
        @DatabaseSyncToAsync
        def get_messages(self, room_name):
            #custom_serializers = CustomSerializer()
            messages = Messages.objects.select_related().filter(discussion__room_name=self.room_name).values(
                    'user__pk',
                    'user__username',
                    'content',
                    'discussion__room_name',
                    'created_at',
            )
            return list(messages) 
        
        @DatabaseSyncToAsync
        def save_message(self, user, content, discussion):
            Messages.objects.create(user=user, content=content, discussion=discussion)
            
        @DatabaseSyncToAsync
        def get_or_create_discussion(self, room_name):
            discussion, created = ZzDiscussions.objects.get_or_create(room_name=room_name)
            return discussion