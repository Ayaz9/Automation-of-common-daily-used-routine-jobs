
# This script helps you to find out count and sum of the numbers that can be divided to the entered number

while True:
    print('Add starting number: ')
    a=int(input())
    print('Add last number: ')
    b=int(input())
    print('Add a number to which one you wanted to divide: ')
    c=int(input())
    total=0
    numbercount=[]
    for num in range(a,b+1):
        if num%c==0:
            numbercount.append(num)
            total+=num
    print("There are "+str(len(numbercount))+" number of "+str(c)+" in between "+str(a)+" and "+str(b)+" and sum of them are: "+str(total))


