
# Here we use ASCII (American Standard Code for Information Interchange) and change input value

# this code encrypts input

while True:
    a=list(input("Enter name to get decrypted name: \n"))
    encryptedname=[]
    for i in a:
        i=ord(i)+25
        encryptedname.append(chr(i))
    print("".join(encryptedname))





# this code decrypts input

while True:
    a=list(input("Enter encrypted name to decrypt it : \n"))
    decryptedname=[]
    for i in a:
        i=ord(i)-25
        decryptedname.append(chr(i))
    print("".join(decryptedname))


