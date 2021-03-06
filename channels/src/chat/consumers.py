import json

from django.contrib.auth import get_user_model

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.db import database_sync_to_async

User = get_user_model()


class ChatConsumer(AsyncConsumer):  # AsyncWebSocketConsumer
    async def websocket_connect(self, event):
        # when the socket connects
        print(event)
        print('-------------------------------')
        
        self.room_name = 'chatter'  # single thread id
        self.room_group_name = f'chat_{self.room_name}'
        self.rando_user = await self.get_name()

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )


        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):  # websocket.receive
        # when the socket receive
        # print(event)
        # print(self.rando_user)
        # message_data = json.loads(event['text'])
        # print(message_data)
        # print('-------------------------------')
        #
        # await self.send({
        #     "type": "websocket.send",
        #     "text": json.dumps(message_data)
        # })
        print(event)
        print('-------------------------------')

        message_data = json.loads(event['text'])
        final_message_data = json.dumps(message_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': final_message_data
            }
        )

    async def chat_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    async def websocket_disconnect(self, event):
        # when the socket disconnects
        print(event)
        print('-------------------------------')

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_name(self):
        return User.objects.all()[0].username
