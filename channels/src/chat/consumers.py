import json

from channels.consumer import SyncConsumer


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # when the socket connects
        print(event)
        print('-------------------------------')
        self.send({
            "type": "websocket.accept"
        })


    def websocket_receive(self, event):  # websocket.receive
        # when the socket receive
        print(event)
        message_data = json.loads(event['text'])
        print(message_data)
        print('-------------------------------')

        self.send({
            "type": "websocket.send",
            "text": json.dumps(message_data)
        })

    def websocket_disconnect(self, event):
        # when the socket disconnects
        print(event)
        print('-------------------------------')
