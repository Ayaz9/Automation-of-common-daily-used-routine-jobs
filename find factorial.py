
# this code will help you to print out factorial of entered number
while True:
    print('Please enter number to find factorial: ')
    a=int(input())
    c=[]
    d=1
    while a>=1:
        c.append(a)
        a-=1
    for i in c:
        d*=i
    print(d)
