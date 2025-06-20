import csv
import time
from random import randint
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest

# Replace these with your actual API credentials
API_ID = 20380321
API_HASH = 'acd2a653b2b4a1720b25b48a7d331e18'
PHONE = "+2347012344623"
# Function to add members to a group

# Persistent session
SESSION_NAME = "new_session_21"  # Change this to a fixed session name

def add_members_to_group(group_username):
    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        try:
            target_group = client.get_entity(group_username)

            with open("members21.csv", "r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)
                usernames = [row["username"] for row in csv_reader if row["username"]]

            for username in usernames:
                try:
                    print(f"Adding {username} to the group...")
                    user = client.get_entity(username)
                    client(InviteToChannelRequest(target_group, [user]))
                    print(f"Successfully added {username}.")

                    # Randomized delay to avoid rate limits
                    delay = randint(20, 30)
                    print(f"Waiting for {delay} seconds...")
                    time.sleep(delay)

                except FloodWaitError as e:
                    print(f"Telegram is rate-limiting. Waiting {e.seconds} seconds before retrying...")
                    time.sleep(e.seconds)

                except UserPrivacyRestrictedError:
                    print(f"Cannot add {username}: Privacy settings restrict this action.")

                except Exception as e:
                    print(f"Failed to add {username}: {e}")

        except Exception as main_error:
            print(f"An error occurred: {main_error}")

# Run the script
if __name__ == "__main__":
    group_username = "@BitclubChatGroup"  # Replace with your group username
    add_members_to_group(group_username)

