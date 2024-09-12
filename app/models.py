from typing import Optional

from pydantic import BaseModel, HttpUrl


class Recipient(BaseModel):
    id: str


class TextMessage(BaseModel):
    text: str


class AttachmentPayload(BaseModel):
    url: HttpUrl
    is_reusable: bool = True


class Attachment(BaseModel):
    type: str
    payload: AttachmentPayload


class Message(BaseModel):
    recipient: Recipient
    message_type: str = "RESPONSE"
    message: Optional[TextMessage] = None
    attachment: Optional[Attachment] = None
