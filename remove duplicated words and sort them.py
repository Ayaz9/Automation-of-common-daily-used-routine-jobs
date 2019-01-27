

# this code accepts words from input with spaces and remove duplicated words and sort them


while True:
    print('please enter words with spaces to remove duplicated ones and sort them')
    a=input()
    # crates the list of words which are given by space
    b=a.split(' ')
    # empty list
    c=[]
    for words in b:
        # comparing the list of words in b with the list of words in c, that means writing the words to new list but eliminating the same words and sorting them
        if words not in c:
            c.append(words)
            c.sort()
    # print out the list of words from c with putting space between them
    print(' '.join(c))
