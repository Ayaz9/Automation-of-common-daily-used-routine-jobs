

# this script helps us to find out current time in requested countries
# in this script we use requests and json modules
import requests, json
# we use API of timezonedb.com to get list of countries with all information in json format, more detail about API of timezonedb.com we can find in https://timezonedb.com/
# using below url we will get list of country time information in json format, by changing json to xml we can get data in xml format ( format=xml
url1 = "http://api.timezonedb.com/v2.1/list-time-zone?key=ZKXCERCSU4ZN&format=json"
response1 = requests.get(url1).text  # using requests module we reach to data of timezonedb.com
jsondata1 = json.loads(response1)  # changing json file to python dictionary format

a = jsondata1["zones"]  # filtering country information from the data which is the value of key : zones, each country information itself also in separate dictionary
countrylist = []  # creating empty list
zonenamelist = []  # creating empty list
# reaching out to each value of list and appending values of each countryName and zoneName to separate list file
for countries in a:
    countrylist.append(countries['countryName'])
for zones in a:
    zonenamelist.append(zones["zoneName"])

while True:
    print('''Please enter country name to find time in that country, please refer to an example how to enter country name : 
Poland''')
# by using try and except method we will skip incorrect entry which may cause and error and inform user to enter correct country name
    try:
        b = countrylist.index(input())  # with user input we will find index of requested country name from list
        c = zonenamelist[b]  # by index we will find zonename of requested country
        # with that zonename, we are able to request time of country using below API request
        # and with Example Poland we are getting the url looks like : http://api.timezonedb.com/v2.1/get-time-zone?key=ZKXCERCSU4ZN&format=json&by=zone&zone=Europe/Warsaw
        url2 = "http://api.timezonedb.com/v2.1/get-time-zone?key=ZKXCERCSU4ZN&format=json&by=zone&zone=" + c
        response2 = requests.get(url2).text
        jsondata2 = json.loads(response2)
        print(jsondata2["formatted"])  # and getting the value of key formatted
    except ValueError:
        print("Oooopss, the entered country name is not correct")

