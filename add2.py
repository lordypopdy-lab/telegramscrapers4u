import csv
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser

# Replace with your API details
API_ID = 24889411
API_HASH = 'dad586a448570799c8e03da26af6f555'
PHONE_NUMBER = +2349051322351

# Target group username or ID
TARGET_GROUP = 'BitclubsCommunity'

# Path to the CSV file containing scraped members
CSV_FILE = 'scraped_members.csv'

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def add_members():
    await client.start(phone=PHONE_NUMBER)

    # Get the target group entity
    group = await client.get_entity(TARGET_GROUP)

    # Read members from the CSV file
    with open(CSV_FILE, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        members = list(csv_reader)

    count = 0
    for member in members:
        try:
            user_id = int(member['user id'])
            access_hash = int(member.get('access hash', 0))  # Some users might not have access hash

            if access_hash:
                user_to_add = InputPeerUser(user_id, access_hash)

                # Add the user to the group
                await client(InviteToChannelRequest(group, [user_to_add]))
                print(f"Added {member['username']} (ID: {user_id}) to the group.")

                count += 1
                if count >= 200:  # Stop after adding 200 users
                    print("Reached the limit of 200 users.")
                    break

                # Delay to avoid hitting Telegram's rate limits
                time.sleep(5)  # Adjust this delay based on actual usage and limits
            else:
                print(f"Skipping {member['username']} due to missing access hash.")

        except Exception as e:
            print(f"Failed to add {member['username']} (ID: {user_id}): {e}")
            # Handle flood wait error
            if 'FloodWaitError' in str(e):
                wait_time = int(str(e).split(' ')[-1])  # Extract wait time
                print(f"Flood wait triggered. Waiting for {wait_time} seconds...")
                time.sleep(wait_time)

    await client.disconnect()

# Run the script
if __name__ == '__main__':
    import asyncio
    asyncio.run(add_members())
