from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

# Replace these with your credentials
phone_number = "+2348162131789"
api_id = 24772601
api_hash = "3132429a348ebdfb0cb6cea6f8100850"
session_name = "new_session_21.session"  # This will store your session file

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
group_link = "@BitclubChat2"  # Replace with actual group link

import asyncio
asyncio.run(join_group(group_link))
