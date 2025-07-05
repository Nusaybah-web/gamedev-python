'''vowls=input("input a sentence: ")

d={"a":0,'e':0,'i':0,'o':0,'u':0}

for i in vowls:
    if i in d:
        d[i]+=1

for key,value in d.items():
    print(key,value)'''


#panagram

'''letters={}

import string

for i in string.ascii_lowercase:
    letters[i]=0

panagram=input()

for i in panagram:
    if i in letters:
        letters[i]+=1

status=True
for i in letters.values():
    if i==0:
        status=False

if status:
    print("it is a panagram")
else:
    print("it is not a panagram")'''

# most frequently used word

words=input()
words=words.lower()
wordlist=words.split()

dictonary={}.fromkeys(wordlist,0)

for i in wordlist:
    if i in dictonary:
        dictonary[i]+=1

print(dictonary)