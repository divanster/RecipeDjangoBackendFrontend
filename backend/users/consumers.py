import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)


class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'users'

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
        try:
            data = json.loads(text_data)
            event_type = data.get('event_type', 'new_user')
            user = data.get('user', {})

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'user': user
                }
            )
        except json.JSONDecodeError:
            logger.error("Received invalid JSON")
            await self.send(text_data=json.dumps({'error': 'Invalid JSON format'}))
        except Exception as e:
            logger.error(f"Error in receive: {str(e)}")
            await self.send(text_data=json.dumps({'error': 'An error occurred'}))

    async def new_user(self, event):
        await self.send(text_data=json.dumps({
            'event': 'new_user',
            'user': event['user']
        }))

    async def update_user(self, event):
        await self.send(text_data=json.dumps({
            'event': 'update_user',
            'user': event['user']
        }))

    async def handle_unknown_event(self, event):
        await self.send(text_data=json.dumps({
            'event': 'unknown_event',
            'error': 'Unknown event type'
        }))
