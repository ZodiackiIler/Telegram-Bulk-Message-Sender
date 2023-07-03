import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')

def send_message(username, message):
    with TelegramClient(phone_number, api_id, api_hash) as client:
        client.send_message(username, message)

filename = 'usernames.txt'
message = 'Ваше сообщение'

with open(filename, 'r') as file:
    usernames = file.read().splitlines()

for username in usernames:
    send_message(username, message)
