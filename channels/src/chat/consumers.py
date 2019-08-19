from channels.consumer import SyncConsumer


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # when the socket connects
        print(event)
        self.send({
            "type": "websocket.accept"
        })
        self.send({
            "type": "websocket.send",
            "text": "Hello websocket"
        })

    def websocket_receive(self, event):
        # when the socket receive
        print(event)

    def websocket_disconnect(self, event):
        # when the socket disconnects
        print(event)
