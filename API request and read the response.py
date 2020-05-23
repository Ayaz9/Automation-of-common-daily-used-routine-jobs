
from urllib import request
import json

token = "Enter your token here"
url = "Enter site url"  # You need to enter your site url
head = {'Authorization': token}
data = {'app': 'aaaaa'}  # this is not mandatory, we can skip this one for now


req = request.Request(url, data=None, headers=head)
response = request.urlopen(req).read().decode('utf-8')   # without decoding, the output is in 'bytes' format

item = list(json.loads(response)['items'])
for meeting_id in item:  # below lines are used for my specific response, you can customize your code differently depending on response
    print("\nMeeting ID : " + meeting_id['id'])
    print("Meeting start time : " + meeting_id['start'])
    print("Meeting Organizer ID : " + meeting_id['organizer'])
    print("Participants lists are: ")
    for participant in meeting_id['encryptedParticipants']:
        print("participant ID: " + participant['id'] +', ' + "type:" + participant['type'] + ", status: " + participant['responseType'])

