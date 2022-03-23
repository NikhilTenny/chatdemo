from cgitb import text
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()   
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)  # Convert to dictionary from json formate
        message = text_data_json['message']

        self.send(text_data = json.dumps({      # Converting a dictionary to json
            'message':message
        }))
