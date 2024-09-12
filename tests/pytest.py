from unittest.mock import AsyncMock, patch

import pytest
from app.main import MessengerAPI


@pytest.mark.asyncio
async def test_send_text_message():
    messenger = MessengerAPI("test_token")
    recipient_id = "123456789"
    text = "Hello, World!"

    with patch('httpx.AsyncClient.post', new_callable=AsyncMock) as mock_post:
        mock_post.return_value.json.return_value = {"recipient_id": recipient_id, "message_id": "msg_id"}
        response = await messenger.send_text_message(recipient_id, text)

        assert response["recipient_id"] == recipient_id
        assert response["message_id"] == "msg_id"
        mock_post.assert_called_once()


@pytest.mark.asyncio
async def test_send_media_message():
    messenger = MessengerAPI("test_token")
    recipient_id = "123456789"
    media_url = "http://example.com/image.jpg"

    with patch('httpx.AsyncClient.post', new_callable=AsyncMock) as mock_post:
        mock_post.return_value.json.return_value = {"recipient_id": recipient_id, "message_id": "msg_id"}
        response = await messenger.send_media_message(recipient_id, media_url)

        assert response["recipient_id"] == recipient_id
        assert response["message_id"] == "msg_id"
        mock_post.assert_called_once()
