# -------------------------------------------------------------------------------------------------------
#  -- import external libraries
import csv
import requests
import json
import settings

# -------------------------------------------------------------------------------------------------------
# -- functions

# get sponsor portal Id

def get_sponsor_portal():

    auth = (ersUsername, ersPassword)
    url = ('https://{}:9060/ers/config/sponsorportal').format(host)
    headers = {'content-type': 'application/json', 'accept': 'application/json'}
    response = requests.get(url, auth=auth, verify=False, headers=headers)
    response_json = json.loads(response.text)
    sponsorPortal = (response_json['SearchResult']['resources'][0]['id'])
    return(sponsorPortal)


# get sponsor Id
def get_sponsorId():

    auth = (ersUsername, ersPassword)
    url = ('https://{}:9060/ers/config/internaluser?name={}').format(host,sponsorUsername)
    headers = {'content-type': 'application/json', 'accept': 'application/json'}
    response = requests.get(url, auth=auth, verify=False, headers=headers)
    response_json = json.loads(response.text)
    sponsorId = (response_json['SearchResult']['resources'][0]['id'])
    return(sponsorId)


# get guest lists from csv file.
def get_guest_list():

    with open('guests.csv', 'r') as f:
        reader = csv.reader(f)
        new_guests = list(reader)

    for guest in new_guests[1:]:
        if len(guest) != 0:
            id = guest
            guestUserId = id[0]
            guestType = id[1]
            status = id[2]
            userName = (id[0])
            firstName = id[3]
            lastName = id[4]
            emailAddress = id[5]
            phoneNumber = id[6]
            password = id[7]

            payload = {
                'GuestUser': {
                    'id': guestUserId,
                    'name': userName,
                    'guestType': guestType,
                    'status': status,
                    'sponsorUserName': sponsorUsername,
                    'sponsorUserId': sponsorId,
                    'guestInfo': {
                        'userName': userName,
                        'firstName': firstName,
                        'lastName': lastName,
                        'emailAddress': emailAddress,
                        'phoneNumber': phoneNumber,
                        'password': password,
                        # 'creationTime': '11/14/2017 12:03',
                        'enabled': 'true',
                        # 'notificationLanguage': 'English',
                        # 'smsServiceProvider': 'Global Default'
                    },
                    'guestAccessInfo': {
                        'validDays': 1,
                        'location': 'San Jose'
                    },
                    'portalId': portalId,
                    'customFields': {},
                    'link': {
                    }
                }
            }
        # print(payload)
        f.close()
    return (payload)


# get accounts
sponsorUsername = settings.sponsorUsername
sponsorPassword = settings.sponsorPassword
ersUsername = settings.ersUsername
ersPassword = settings.ersPassword
host = settings.host


# -------------------------------------------------------------------------------------------------------
# -- main code
# create guest account and show status
#
portalId = get_sponsor_portal()
print('\nStatus...Getting Sponsor Portal ID: {}'.format(portalId))

sponsorId = get_sponsorId()
print('\nStatus...Getting Sponsor ID: {}'.format(sponsorId))

guest_payload = get_guest_list()
payload = guest_payload
print('\nStatus...Getting Guest List: {}'.format(payload))

headers = {
    'content-type': 'application/json',
    'accept': 'application/json'
}

auth = (sponsorUsername, sponsorPassword)

url = 'https://{}:9060/ers/config/guestuser'.format(host)
response = requests.post(url, auth=auth, data=json.dumps(payload), headers=headers, verify=False)


if response.status_code == 201:
    print ('Account created by {}\n'.format(sponsorUsername))

elif response.status_code == 400:
    status = json.loads(response.text)
    print ('Error:',status['ERSResponse']['messages'][0]['title'])

print ('\nEnd')
