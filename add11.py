# import csv
# import time
# from random import randint
# from telethon.sync import TelegramClient
# from telethon.errors import FloodWaitError, UserPrivacyRestrictedError
# from telethon.tl.functions.channels import InviteToChannelRequest

# # Replace these with your actual API credentials
# API_ID = 26072830
# API_HASH = '38cd1eaa0fdd8cd744a7af142d7c7c9f'
# PHONE = "+2348026073878"

# # Persistent session
# SESSION_NAME = "new_session_11"  # Change this to a fixed session name

# def add_members_to_group(group_username):
#     with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
#         try:
#             target_group = client.get_entity(group_username)

#             with open("members11.csv", "r", encoding="utf-8") as file:
#                 csv_reader = csv.DictReader(file)
#                 usernames = [row["username"] for row in csv_reader if row["username"]]

#             for username in usernames:
#                 try:
#                     print(f"Adding {username} to the group...")
#                     user = client.get_entity(username)
#                     client(InviteToChannelRequest(target_group, [user]))
#                     print(f"Successfully added {username}.")

#                     # Randomized delay to avoid rate limits
#                     delay = randint(20, 30)
#                     print(f"Waiting for {delay} seconds...")
#                     time.sleep(delay)

#                 except FloodWaitError as e:
#                     print(f"Telegram is rate-limiting. Waiting {e.seconds} seconds before retrying...")
#                     time.sleep(e.seconds)

#                 except UserPrivacyRestrictedError:
#                     print(f"Cannot add {username}: Privacy settings restrict this action.")

#                 except Exception as e:
#                     print(f"Failed to add {username}: {e}")

#         except Exception as main_error:
#             print(f"An error occurred: {main_error}")

# # Run the script
# if __name__ == "__main__":
#     group_username = "@BitclubChatGroup"  # Replace with your group username
#     add_members_to_group(group_username)


    

import csv
import time
from random import randint
from telethon.sync import TelegramClient
from telethon.errors import (
    FloodWaitError, UserPrivacyRestrictedError,
    PeerFloodError, ChatWriteForbiddenError
)

# === Your Telegram API credentials ===
API_ID = 26072830
API_HASH = '38cd1eaa0fdd8cd744a7af142d7c7c9f'
SESSION_NAME = "new_session_11"  # Persistent session

# === BITCLUB Message ===
INVITE_LINK = "https://t.me/BitclubChatGroup"  # Your actual group link
MESSAGE = (
    "🚀 Join BITCLUB — the most active crypto hub for traders, airdrops, "
    "free signals, and market insights. Engage, earn, and grow. Tap to enter: " + INVITE_LINK
)

def dm_users():
    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        with open("members11.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            usernames = [row["username"].strip().lstrip("@") for row in csv_reader if row.get("username")]

        print(f"📬 Starting DM session. Loaded {len(usernames)} users.")

        for username in usernames:
            try:
                print(f"📨 Sending message to {username}...")
                user = client.get_entity(username)
                client.send_message(user, MESSAGE)
                print(f"✅ Sent to {username}.")

                # Delay to avoid flood limits
                delay = randint(30, 50)
                print(f"⏳ Waiting {delay} seconds...\n")
                time.sleep(delay)

            except UserPrivacyRestrictedError:
                print(f"🔒 Cannot message {username}: Privacy settings blocked DMs.")
            except ChatWriteForbiddenError:
                print(f"❌ Cannot message {username}: You don't have permission.")
            except PeerFloodError:
                print("🚨 Too many DMs sent. Telegram has rate-limited your account. Try again later.")
                break
            except FloodWaitError as e:
                print(f"🚦 Flood wait active. Waiting {e.seconds} seconds...")
                time.sleep(e.seconds)
            except Exception as e:
                print(f"⚠️ Failed to message {username}: {e}")

# === Run the script ===
if __name__ == "__main__":
    dm_users()
