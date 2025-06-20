# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script
# from telethon.sync import TelegramClient
# from telethon.tl.functions.messages import GetDialogsRequest
# from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
# from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, InviteHashExpiredError, ChannelPrivateError, UserAlreadyParticipantError
# from telethon.tl.functions.channels import InviteToChannelRequest
# from telethon.tl.functions.messages import ImportChatInviteRequest
# from telethon.tl.functions.channels import JoinChannelRequest
# from telethon import types
# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script
# import sys
# import csv
# import os
# import subprocess
# import configparser
# import traceback
# import time
# from telethon.sessions import StringSession

# lines = list()

# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script

# SLEEP_TIME_1 = 10
# SLEEP_TIME_2 = 3
# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script
# def filterall():
#     def main():
#         with open('teammember.csv', 'r', encoding='UTF-8') as readFile:

#             reader = csv.reader(readFile)

#             for row in reader:

#                 lines.append(row)

#                 for field in row:

#                     if field == '':
#                         lines.remove(row)
#                     if field == 'username':
#                         lines.remove(row)

#         with open('Final.csv', 'w', encoding='UTF-8') as writeFile:
#             writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

#             writer.writerows(lines)

#     main()
#     with open('Final.csv', 'w', encoding='UTF-8') as writeFile:
#         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

#         writer.writerows(lines)

#     myfile = "teammember.csv"
# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script
#     ## If file exists, delete it ##
#     if os.path.isfile(myfile):
#         os.remove(myfile)
#     else:  ## Show an error ##
#         print("Error: %s file not found" % myfile)

#     with open("Final.csv", "r", encoding='UTF-8') as source:
#         rdr = csv.reader(source)

#         with open("teammember.csv", "w", encoding='UTF-8') as f:
#             writer = csv.writer(f, delimiter=",", lineterminator="\n")
#             writer.writerow(['sr. no.', 'username', 'user id', 'name', 'Status'])
#             i = 0
#             for row in rdr:
#                 i += 1
#                 writer.writerow((i, row[1], row[2], row[3], row[4]))
#         print('')
#         print("Waiting {} Seconds, Removing user without username!".format(SLEEP_TIME_2))
#         time.sleep(SLEEP_TIME_2)
#         print('')
# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script
#     myfile = "Final.csv"

#     ## If file exists, delete it ##
#     if os.path.isfile(myfile):
#         os.remove(myfile)
#     else:  ## Show an error ##
#         print("Error: %s file not found" % myfile)
#     print("Successfully Filtered And Saved In teammember.csv")
#     input('Please ENTER to exit..')

# filterall()
# #Coded with Solved4You 
# #Subscribe for more Free Telegram Script


import csv
import os
import time

# Constants for sleep times
SLEEP_TIME_1 = 10
SLEEP_TIME_2 = 3

def filter_csv():
    input_file = "XM.csv"
    output_file = "Final.csv"
    final_filtered_file = "XM.csv"
    
    # Read and filter data
    filtered_data = []
    with open(input_file, 'r', encoding='UTF-8') as read_file:
        reader = csv.reader(read_file)
        header = next(reader, None)  # Read header
        
        for row in reader:
            if row and row[0] and row[0] != "username":  # Ignore empty and header rows
                filtered_data.append(row)
    
    # Write filtered data to Final.csv
    with open(output_file, 'w', encoding='UTF-8', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(filtered_data)
    
    # Write to teammember.csv with new headers
    with open(final_filtered_file, 'w', encoding='UTF-8', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(['sr. no.', 'username', 'user id', 'name', 'Status'])
        
        for i, row in enumerate(filtered_data, start=1):
            writer.writerow([i, row[0], row[2], row[1], row[6]])
    
    print(f"Waiting {SLEEP_TIME_2} seconds, removing user without username!")
    time.sleep(SLEEP_TIME_2)
    
    # Remove Final.csv as it's no longer needed
    if os.path.exists(output_file):
        os.remove(output_file)
    
    print("Successfully filtered and saved in teammember.csv")
    input("Press ENTER to exit...")

filter_csv()
