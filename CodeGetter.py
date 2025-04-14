from telethon import TelegramClient, events
import re

api_id = 25938607
api_hash = 'd122ec7a5cf39942e27c4adcb5b6b192'

client = TelegramClient('new_session_6', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    sender_name = sender.username or sender.first_name or "Unknown"
    text = event.message.text
    print(f"📩 New message from {sender_name}: {text}")

    if sender.username == 'Telegram':
        match = re.search(r'(\d{5})', text)
        if match:
            code = match.group(1)
            print("🔐 Login code:", code)

client.start()
print("✅ Listening for messages...")
client.run_until_disconnected()
