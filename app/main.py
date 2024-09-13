import logging

from fastapi import FastAPI

from app.messenger import MessengerAPI
from app.models import TextMessage
from config.settings import settings

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Happy coding, Eastwesser!"}


@app.post("/send-message/")
async def send_message(message: TextMessage):
    logging.info(f"Received message payload: {message}")
    messenger = MessengerAPI(page_access_token=settings.page_access_token)
    response = await messenger.send_text_message(message.recipient_id, message.text)
    logging.info(f"Message sent with response: {response}")
    return response
