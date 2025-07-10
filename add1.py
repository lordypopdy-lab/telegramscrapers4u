import csv
import time
from random import randint
from telethon.sync import TelegramClient
from telethon.errors import (
    FloodWaitError, UserPrivacyRestrictedError,
    PeerFloodError, ChatWriteForbiddenError
)
from telethon.tl.functions.contacts import DeleteContactsRequest
from telethon.tl.functions.users import GetFullUserRequest

API_ID = 20306541
API_HASH = 'da7c1082b65503ec2f9160d732e352f9'
TOTAL_SESSIONS = 21
CSV_FILE = "members1.csv"
INVITE_LINK = "https://t.me/BitclubChatGroup"
MESSAGE = (
    "🚀 Join BITCLUB — the most active crypto hub for traders, airdrops, "
    "free signals, and market insights. Engage, earn, and grow. 👉: " + INVITE_LINK
)

# Load usernames from CSV
def load_usernames():
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        return [row["username"].strip().lstrip("@") for row in csv.DictReader(file) if row.get("username")]

# Save back only unprocessed usernames to the original CSV
def update_csv(remaining_usernames):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["username"])
        for username in remaining_usernames:
            writer.writerow([username])

# Append to success or fail logs
def log_result(filename, username, reason=""):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, reason])

# DM logic per user per session
def dm_user_with_session(session_name, username):
    with TelegramClient(session_name, API_ID, API_HASH) as client:
        try:
            print(f"📨 Sending message to {username} using {session_name}...")
            user = client.get_entity(username)
            client.send_message(user, MESSAGE)
            print(f"✅ Sent to {username}")
            log_result("dm_success.csv", username)
        except UserPrivacyRestrictedError:
            print(f"🔒 {username}: Privacy restriction")
            log_result("dm_failed.csv", username, "Privacy Restricted")
        except ChatWriteForbiddenError:
            print(f"❌ {username}: DM permission denied")
            log_result("dm_failed.csv", username, "No Permission")
        except PeerFloodError:
            print(f"🚨 {session_name}: Rate limit hit")
            return "RATE_LIMITED"
        except FloodWaitError as e:
            print(f"⏳ Flood wait: {e.seconds} sec")
            time.sleep(e.seconds)
            return dm_user_with_session(session_name, username)
        except Exception as e:
            print(f"⚠️ Failed for {username}: {e}")
            log_result("dm_failed.csv", username, str(e))
        finally:
            try:
                user = client.get_entity(username)
                full = client(GetFullUserRequest(user))
                client(DeleteContactsRequest([user]))
                print(f"🗑️ Deleted contact {username}")
            except:
                print(f"⚠️ Could not delete contact {username}")

    delay = randint(25, 40)
    print(f"⏳ Sleeping {delay} seconds...\n")
    time.sleep(delay)
    return "OK"

# Main handler
def dm_users():
    usernames = load_usernames()
    remaining_usernames = usernames.copy()
    session_index = 1

    for username in usernames:
        while session_index <= TOTAL_SESSIONS:
            session_name = f"new_session_{session_index}"
            result = dm_user_with_session(session_name, username)

            if result == "OK" or result == "RATE_LIMITED":
                if username in remaining_usernames:
                    remaining_usernames.remove(username)
                if result == "RATE_LIMITED":
                    session_index += 1
                break

        if session_index > TOTAL_SESSIONS:
            print("🚫 All sessions rate-limited. Halting.")
            break

    update_csv(remaining_usernames)

# Run it
if __name__ == "__main__":
    dm_users()
