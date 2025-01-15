import csv
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# Replace with your API details
API_ID = 23961419
API_HASH = 'e0946bec453fad0d57b30d55dbcadc96'
PHONE_NUMBER = +2348038239730

# Target group username or ID
TARGET_GROUP = 'apeandpepe'

# Output CSV file
CSV_FILE = 'scraped_members.csv'

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def scrape_members():
    await client.start(phone=PHONE_NUMBER)

    # Get the target group entity
    group = await client.get_entity(TARGET_GROUP)

    # Fetch group participants
    participants = await client(GetParticipantsRequest(
        channel=group,
        filter=ChannelParticipantsSearch(''),
        offset=0,
        limit=10000,
        hash=0  # Default value for hash
    ))

    # Open CSV file for writing
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['sr. no.', 'username', 'user id', 'name', 'status'])

        for index, participant in enumerate(participants.users, start=1):
            username = participant.username or ''
            user_id = participant.id
            access_hash = participant.access_hash or ''
            name = f"{participant.first_name or ''} {participant.last_name or ''}".strip()
            status = 'Active' if participant.status else 'Inactive'

            # Write participant details to CSV
            writer.writerow([index, username, user_id, name, status])

            print(f"Scraped: {username} (ID: {user_id})")

    print(f"Scraping complete. Data saved to {CSV_FILE}")
    await client.disconnect()

# Run the script
if __name__ == '__main__':
    import asyncio
    asyncio.run(scrape_members())
