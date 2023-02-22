from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import time
import json


class StudentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = "Student"
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
    
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            self.username = text_data_json['username']
            self.command = text_data_json['command']
            print(self.username)
            print(self.group_name)
            if self.command == "python":
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type':'change',
                        'text' : "python shell has been open."
                    }
                )
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def change(self, event):
        self.send(text_data=event['text'])
        count = 0
        while True:
            time.sleep(5)
            self.send("you are using python shell - server. 5/s !")
            count += 1
            if count == 5:
                break
        self.close()
