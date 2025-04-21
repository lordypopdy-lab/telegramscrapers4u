from telethon import TelegramClient, events
import re

api_id = 24772601
api_hash = '3132429a348ebdfb0cb6cea6f8100850'

client = TelegramClient('new_session_21', api_id, api_hash)

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
