from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

# Replace these with your credentials
phone_number = "+2349031415958"
api_id = 22737247
api_hash = "5f4a3178c89e34aefc9027c3f04a98be"
session_name = "new_session_45"  # This will store your session file

# Initialize Telethon client
client = TelegramClient(session_name, api_id, api_hash)

async def join_group(group_link):
    async with client:
        try:
            await client(JoinChannelRequest(group_link))
            print(f"Successfully joined: {group_link}")
        except Exception as e:
            print(f"Error: {e}")

# Provide the group username or invite link
group_link = "@BitclubCryptoNews"  # Replace with actual group link

import asyncio
asyncio.run(join_group(group_link))
