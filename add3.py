import csv
import time
from random import randint
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

# Replace these with your actual API credentials
API_ID = 21956695
API_HASH = '299d9f260fcd28963bc4d0bab7ad6351'
PHONE = "+2349020234290"
# Function to add members to a group
def add_members_to_group(group_username):
    # Initialize the client
    with TelegramClient('new_session_3', API_ID, API_HASH) as client:
        try:
            # Get the target group entity
            target_group = client.get_entity(group_username)

            # Read members from the CSV file
            with open('members3.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                usernames = [row['username'] for row in csv_reader if row['username']]

            # Adding members to the group
            for username in usernames:
                try:
                    print(f"Adding {username} to the group...")
                    user = client.get_entity(username)
                    client(InviteToChannelRequest(target_group, [user]))
                    print(f"Successfully added {username}.")
                    
                    # Random delay to avoid flood errors
                    delay = randint(20, 30)  # Random delay between 5 to 10 seconds
                    print(f"Waiting for {delay} seconds...")
                    time.sleep(delay)

                except Exception as e:
                    print(f"Failed to add {username}: {e}")

        except Exception as main_error:
            print(f"An error occurred: {main_error}")

# Example usage
if __name__ == "__main__":
    group_username = "@BitclubsChannell"  # Replace with the target group's username
    add_members_to_group(group_username)
