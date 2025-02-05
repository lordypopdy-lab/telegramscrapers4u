#this code is arranged by Solved4You 2.0
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time

#account details
api_id = 23961419
api_hash = 'e0946bec453fad0d57b30d55dbcadc96'
phone = +2348038239730

session_name = 'scraper' #means that this session_name is for scraper
#this code is arranged by Solved4You 2.0
client = TelegramClient(str(session_name), api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members...')
all_participants = []

#enter target group or channel
target = 'https://t.me/cursosja'
#this code is arranged by Solved4You 2.0
all_participants = client.get_participants(target, aggressive=True)
#this code is arranged by Solved4You 2.0
print('Saving In file...')
with open("membersNew.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['sr. no.','username', 'user id', 'name', 'group', 'group id'])
    i = 0
    for user in all_participants:

        i += 1
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([i,username, user.id, name, 'group name', 'groupid'])
print('Members scraped successfully.')

#this code is arranged by Solved4You 2.0