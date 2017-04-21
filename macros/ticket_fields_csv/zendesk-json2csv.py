import os
from getpass import getpass
import json
import csv

localfolder = os.path.dirname(os.path.realpath(__file__))

down = input("Would you like to dowload ticket data from Zendesk now? (y/n)")
if down in ["Y", "y"]:
    print("Please input your Zendesk credentials")
    email = input("E-mail address:")
    pword = getpass()
    curl = os.path.join(localfolder, "curl.exe")
    os.system(curl + " https://camacuk.zendesk.com/api/v2/ticket_fields.json -v -u " + email + ":" + pword + " > data.json")

    
with open(os.path.join(localfolder, 'data.json')) as data_file:
    data = json.load(data_file)

with open('ticket_fields.csv', 'w') as csvfile:
    fieldnames = ['title_in_portal', 'id', 'active', 'url']#, 'raw_title', 'created_at', 'description', 'title', 'visible_in_portal', 'raw_description', 'required', 'updated_at', 'required_in_portal', 'collapsed_for_agents', 'regexp_for_validation', 'tag', 'raw_title_in_portal', 'position', 'removable', 'type', 'editable_in_portal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore', lineterminator = '\n')
    writer.writeheader()
    
    fields = data["ticket_fields"]
    for a in fields:
        writer.writerow(a)