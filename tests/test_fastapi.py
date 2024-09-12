from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

import pytest
from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_send_message_endpoint():
    recipient_id = "123456789"
    text = "Hello, World!"

    with patch("app.messenger.MessengerAPI.send_text_message", new_callable=AsyncMock) as mock_send_message:
        mock_send_message.return_value = {"recipient_id": recipient_id, "message_id": "msg_id"}

        response = client.post("/send-message/", json={"recipient_id": recipient_id, "text": text})

        assert response.status_code == 200
        data = response.json()
        assert data["recipient_id"] == recipient_id
        assert data["message_id"] == "msg_id"
