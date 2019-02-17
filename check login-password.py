
# this code checks entered login/password by giving the user 10 attempts chances
# stdiomask module is used to hide input password, re module is used to match specific password requirement
import stdiomask,re
cl='ayaz' # this is random user name is given, you can change it to whatever you want
cp='Poland2019!' # this is random password, make sure criteria is matching
i=0
while i<10:
    print('You have '+str(10-i)+' chance')
    a=input('login: ')
    while True:
        b=stdiomask.getpass(mask="X") # we can change mask value to anything we want, by default (no mask) it is *
        if len(b)<8:
            print("Minimum password length must be 8 characters")
        elif re.search("[0-9]",b) is None:
            print("Minimum one digit is required")
        elif re.search("[A-Z]", b) is None:
            print("Minimum one capital is required")
        else:
            break
    if i==9 and a!=cl or i==9 and b!=cp:
        print('Please contact with site admin')
    elif a!=cl and b==cp:
        print('Password is correct and Login is incorrect')
    elif b!=cp and a==cl:
        print('Login is correct and Password is incorrect')
    elif a!=cl and b!=cp:
        print('Login and password are incorrect')    
    elif a==cl and b==cp:
        print('Access granted')
        break
    i+=1
input('Press enter to close the program')
