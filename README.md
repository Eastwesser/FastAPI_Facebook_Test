# FastAPI Facebook Messenger API

This is a simple project that integrates FastAPI with the Facebook Messenger API. 
The application allows sending text and media messages to users on Facebook Messenger using the official API.

## Features
- Send text messages to Facebook Messenger users.
- Send media messages (images, videos, etc.) via Facebook Messenger.

## Technologies Used
- FastAPI: A modern web framework for building APIs with Python.
- Facebook Messenger API: For interacting with Facebook Messenger.
- Pydantic: Data validation using Python models.
- aiohttp: Asynchronous HTTP client for making requests to the Facebook API.
- python-dotenv: For loading environment variables from a .env file.

## Project Structure

```bash
FastAPI_Facebook_Test
├── app
│   ├── __init__.py
│   ├── main.py          # Main application file
│   ├── messenger.py     # Facebook Messenger API logic
│   └── models.py        # Pydantic models for validation
├── config
│   └── settings.py      # Project settings and environment variable management
├── .env                 # Environment variables
└── requirements.txt     # Python dependencies
```

## Prerequisites
Before running this project, ensure you have the following installed:

- Python 3.10 or higher.
- A valid Facebook Page Access Token for the Facebook Messenger API.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Eastwesser/FastAPI_Facebook_Test.git
cd FastAPI_Facebook_Test
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  
# On Windows: .\venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a .env file in the root of your project (if it doesn't exist), and add the following:
```ini
PAGE_ACCESS_TOKEN=your_facebook_page_access_token_here
API_VERSION=v20.0
DEBUG=True
```

5. Run the application: You can run the application using uvicorn:
```bash
uvicorn app.main:app --reload
```
The app will be running at http://127.0.0.1:8000.

## API Endpoints

1. Root (/)
Method: GET
Description: A simple health check endpoint to verify that the API is working.
Response:
```json
{
  "message": "Hello, World!"
}
```

2. Send Message (/send-message/)
Method: POST
Description: Send a text message to a user on Facebook Messenger.
Request Parameters:
- recipient_id (string): The Facebook user ID of the recipient.
- text (string): The text message to send.
Example Request:
```json
{
  "recipient_id": "1234567890",
  "text": "Hello, this is a test message!"
}
```
Example Response:
```json
{
  "recipient_id": "1234567890",
  "message_id": "mid.$cAAD..."
}
```
