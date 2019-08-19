import json

from django.contrib.auth import get_user_model

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.db import database_sync_to_async

User = get_user_model()


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        # when the socket connects
        print(event)
        print('-------------------------------')
        self.rando_user = await self.get_name()

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):  # websocket.receive
        # when the socket receive
        print(event)
        print(self.rando_user)
        message_data = json.loads(event['text'])
        print(message_data)
        print('-------------------------------')

        await self.send({
            "type": "websocket.send",
            "text": json.dumps(message_data)
        })

    async def websocket_disconnect(self, event):
        # when the socket disconnects
        print(event)
        print('-------------------------------')

    @database_sync_to_async
    def get_name(self):
        return User.objects.all()[0].username
