
import json
import os
import requests

# BOT_TOKEN ko environment variables se securely lena
BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def handler(event, context):
    try:
        # Telegram se aaye data ko padhna
        body = json.loads(event.get('body', '{}'))
        message = body.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        user_text = message.get('text', '')

        # Agar chat_id ya text nahi mila, to ignore karo
        if not chat_id or not user_text:
            return {'statusCode': 200, 'body': 'Not a message to process'}

        # User ko wahi message wapas bhejna (Echo Bot)
        response_text = f"Aapne bheja: {user_text}"

        # Telegram ko message bhejne ke liye data taiyar karna
        payload = {
            'chat_id': chat_id,
            'text': response_text
        }

        # Telegram API ko request bhejna
        requests.post(TELEGRAM_URL, json=payload)

        # Netlify ko batana ki sab theek tha
        return {'statusCode': 200, 'body': 'Message sent'}

    except Exception as e:
        # Agar koi error aaye to use print karna (debugging ke liye)
        print(f"Error: {e}")
        return {'statusCode': 500, 'body': 'An error occurred'}

