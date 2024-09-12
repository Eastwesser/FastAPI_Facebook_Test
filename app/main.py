import logging

from fastapi import FastAPI

from app.messenger import MessengerAPI
from config.settings import settings

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.post("/send-message/")
async def send_message(recipient_id: str, text: str):
    logging.info(f"Sending message to recipient: {recipient_id}")
    messenger = MessengerAPI(page_access_token=settings.page_access_token)
    response = await messenger.send_text_message(recipient_id, text)
    logging.info(f"Message sent with response: {response}")
    return response
