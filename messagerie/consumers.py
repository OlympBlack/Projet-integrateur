from channels.generic.websocket import WebsocketConsumer
import json

class MessagerieConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    """async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envoyer le message au serveur Django
        await self.send(text_data=json.dumps({
            'message': message
        }))"""