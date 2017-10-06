#!/usr/bin/python3
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

from settings import API_ID, API_HASH, PHONE

# (1) Use your own values here
api_id = API_ID
api_hash = API_HASH
phone = PHONE
session_name = str(api_id)

# (2) Create the client and connect
client = TelegramClient(session_name, api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# (3) Using built-in methods
dialogs, entities = client.get_dialogs(10)
print(entities)
entity = entities[0]

# (4) !! Invoking a request manually !!
result = client(GetHistoryRequest(
    entity,
    limit=20,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0
))

# Now you have access to the first 20 messages
messages = result.messages

print(messages)