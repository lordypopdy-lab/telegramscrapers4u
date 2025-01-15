import csv
import time
from random import randint
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import UserPrivacyRestrictedError, FloodWaitError, PeerFloodError

# Replace these with your actual API credentials
API_ID = 24950098
API_HASH = '490ea55cf4898ca58744698726b0a8fb'
PHONE = '+2349163309961'

# Function to add members to a group
def add_members_to_group(group_username, daily_limit=50):
    # Initialize the client
    with TelegramClient('new_session_name', API_ID, API_HASH) as client:
        try:
            # Get the target group entity
            target_group = client.get_entity(group_username)

            # Read members from the CSV file
            with open('members.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                usernames = [row['username'] for row in csv_reader if row['username']]

            added_count = 0  # Track the number of users added
            for username in usernames:
                if added_count >= daily_limit:
                    print("Daily limit reached. Stopping the process.")
                    break

                try:
                    print(f"Adding {username} to the group...")
                    user = client.get_entity(username)
                    client(InviteToChannelRequest(target_group, [user]))
                    print(f"Successfully added {username}.")

                    added_count += 1
                    
                    # Random delay to mimic human behavior
                    delay = randint(45, 90)  # Delay between 45 to 90 seconds
                    print(f"Waiting for {delay} seconds...")
                    time.sleep(delay)

                except UserPrivacyRestrictedError:
                    print(f"Cannot add {username}: Privacy settings restrict adding.")
                except FloodWaitError as e:
                    wait_time = int(e.seconds)
                    print(f"Flood wait error! Waiting for {wait_time} seconds...")
                    time.sleep(wait_time)
                except PeerFloodError:
                    print("PeerFloodError encountered. Stopping to prevent account issues.")
                    break
                except Exception as e:
                    print(f"Failed to add {username}: {e}")

        except Exception as main_error:
            print(f"An error occurred: {main_error}")

# Example usage
if __name__ == "__main__":
    group_username = "BitclubsChannel"  # Replace with the target group's username
    add_members_to_group(group_username)
