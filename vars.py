#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26597954"))
API_HASH = environ.get("API_HASH", "716dc5f8ceaecef896701f9e846bb328")
BOT_TOKEN = environ.get("BOT_TOKEN", "8497384947:AAGl38n9kN0EalXWrv7ANE0lN8DC2hUNdWM")

OWNER = int(environ.get("OWNER", "7516538361"))
CREDIT = environ.get("CREDIT", "𝑷𝑹𝑶𝑭𝑬𝑺𝑺𝑶𝑹 𝑩𝑶𝑻𝑺")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

