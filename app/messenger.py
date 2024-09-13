from aiohttp import ClientSession

from app.models import (
    Message,
    Recipient,
    TextMessage,
    Attachment,
    AttachmentPayload,
)


class MessengerAPI:
    def __init__(self, page_access_token: str):
        self.page_access_token = page_access_token
        self.base_url = "https://graph.facebook.com/v20.0/me/messages"

    async def send_message(self, recipient_id: str, message: str) -> dict:
        payload = Message(
            recipient=Recipient(id=recipient_id),
            message=TextMessage(text=message),
        ).dict()

        async with ClientSession() as session:
            async with session.post(
                    self.base_url,
                    params={"access_token": self.page_access_token},
                    json=payload,
            ) as response:
                return await response.json()

    async def send_text_message(self, recipient_id: str, text: str) -> dict:
        return await self.send_message(recipient_id, text)

    async def send_media_message(self, recipient_id: str, media_url: str, media_type: str) -> dict:
        payload = Message(
            recipient=Recipient(id=recipient_id),
            attachment=Attachment(
                type=media_type,
                payload=AttachmentPayload(url=media_url),
            )
        ).dict()

        async with ClientSession() as session:
            async with session.post(
                    self.base_url,
                    params={"access_token": self.page_access_token},
                    json=payload,
            ) as response:
                return await response.json()
