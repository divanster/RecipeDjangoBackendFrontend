# backend/pages/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'pages'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'page_message',
                'message': data['message']
            }
        )

    async def page_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
