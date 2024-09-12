from unittest.mock import AsyncMock, patch

import pytest
from app.messenger import MessengerAPI


@pytest.mark.asyncio
async def test_send_text_message():
    messenger = MessengerAPI("test_token")
    recipient_id = "123456789"
    text = "Hello, World!"

    # Мокаем HTTP-запрос
    with patch("aiohttp.ClientSession.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value.__aenter__.return_value.json.return_value = {"recipient_id": recipient_id,
                                                                            "message_id": "msg_id"}

        response = await messenger.send_text_message(recipient_id, text)

        # Проверка ответа
        assert response["recipient_id"] == recipient_id
        assert response["message_id"] == "msg_id"
        mock_post.assert_called_once()


@pytest.mark.asyncio
async def test_send_media_message():
    messenger = MessengerAPI("test_token")
    recipient_id = "123456789"
    media_url = "http://example.com/image.jpg"

    # Мокаем HTTP-запрос
    with patch("aiohttp.ClientSession.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value.__aenter__.return_value.json.return_value = {"recipient_id": recipient_id,
                                                                            "message_id": "msg_id"}

        response = await messenger.send_media_message(recipient_id, media_url, "image")

        # Проверка ответа
        assert response["recipient_id"] == recipient_id
        assert response["message_id"] == "msg_id"
        mock_post.assert_called_once()
