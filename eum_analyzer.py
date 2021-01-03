import re

'''
The flow is like the following : 
#1 - search errors and if any match, print relative actions
#2 - search Registered Records, and if any match, then search relative app_key&account and time
#3 - for step #2, first print time, then app_key&account and then Registered record 
#4 - then we search Received or Dropped events and printing them
'''

# with the help of below function we search errors in every lines. Errors are the keys of dict


def errors_and_actions():  # line here means every line of the log file
    file = open('eum-processor.log', 'r').readlines()
    errors_actions = {'Error publishing analytics events': 'Check why could not execute the request to Events Service',}  # this dict keys contain errors and value contains action for the found errors
    # looking for dict keys in each lines, and if finds any match, then printing error line and action relatively.
    for line in file:
        for error in errors_actions.keys():
            if re.search(error, line):
                print('ERROR : ' + line + '\n' + 'ACTION : ' + errors_actions[error] + '\n' * 2 + '*' * 30)


errors_and_actions()


def find_registered_appkey_account(line):  # here we find registered app key and account
    file = open('eum-processor.log', 'r').readlines()
    appkey_account_pattern = 'App=.*, Account=.*'  # pattern to find appkey and account
    n = 0
    while n < 30:  # here we put loop to look at previous lines to find appkey and account for the registered record
        match = re.search(appkey_account_pattern, file[file.index(line) - n])
        if match:
            # print(match.group(0))  # added as test purpose
            return 'App_Key and Account : ' + str(match.group(0))
        n += 1


def find_received_dropped_time(line):  # here we find the time stamp for received/dropped events
    file = open('eum-processor.log', 'r').readlines()
    time_pattern = '^\d{1,2}.*\d{1,4} \d{1,2}:\d{1,2}:\d{1,2}.\d{1,4} \+\d{1,4}'
    n = 0
    while n < 30:
        match = re.search(time_pattern, file[file.index(line) - n])
        if match:
            return 'TIME : ' + str((re.search(time_pattern, file[file.index(line) - n])).group(0))
        n += 1


def find_registered_records():  # this function defines if there is any registered record
    file = open('eum-processor.log', 'r').readlines()
    registered_pattern = '(REGISTERED .*: )(\d)'  # I'll use second group which is number
    registered_list = []
    for i in file:
        match = re.search(registered_pattern, i)
        if match and match.group(2) != 0:  # example : REGISTERED BrowserRecord BASE_PAGE: 1 (here number 1 is second group of regex)
            print(find_received_dropped_time(i))  # printing registered time
            print(find_registered_appkey_account(i))  # printing registered appkey&account
            registered_list.append('Registered record is : ' + i)  # here we are adding the Records to the list
            print(i)  # registered record line
    if not registered_list:
        return 'There are NO registered records'


find_registered_records()


def find_received_dropped():  # here we find received or dropped events. Example :  |		Received = 215, Dropped = 0, Persisted = 219, Checkpointed = 0
    file = open('eum-processor.log', 'r').readlines()
    received_dropped_pattern = '(.*Received = )(\d+)(, Dropped = )(\d+)(.*)'  # if group 2 matches, this means there is
    # received packets, if group 4 matches, this means there are packets dropped
    received = []
    dropped = []
    for i in file:
        match = re.search(received_dropped_pattern, i)
        if match and int(match.group(2)) != 0 and int(match.group(4)) == 0:
            # print(type(match.group(2)))  # it's for test reason and type is string
            received.append(i)  # here we add received events to the list
        elif match and int(match.group(2)) == 0 and int(match.group(4)) != 0:
            # print(find_received_dropped_time(i))
            dropped.append(i)  # here we add dropped events to the list
        #  I'll think to add third condition which is having both received and dropped events
    if received:
        return '\n' * 2 + 'RECEIVED : ' + '\n'.join(received)  # this will return received events
    elif dropped:
        return '\n' * 2 + 'DROPPED : ' + '\n'.join(dropped)  # this will return dropped events
    else:
        return '\n' * 2 + 'There are NO any Received or Dropped events (example : Received = 0, Dropped = 0)!'


print(find_received_dropped())


