

# This code pings ololo.host every 5 mins and stores results in Database folder

import subprocess,os,time, datetime
while True:
    # wait 5 mins ( 300 secs ) and run script again
    time.sleep(300)
    # ping the ololo.host and assign it to variable result
    result = subprocess.check_output(['ping', 'ololo.host'])
    # I put my direction, you can change it as well
    os.chdir('C:\\Users\\abayramo\\Desktop\\my files\\python\\DataBase')
    # open new.txt file in append mode
    ping_result=open("new.txt", "a")
    # learn and write current time stamp
    current_time = datetime.datetime.now()
    ping_result.write('''
    **********************************************************************
    '''+'\n*2'+str(current_time)+'\n'*2)
    # write ping result to new.txt file
    ping_result.write(str(result))
    # close new.txt file
    ping_result.close()






