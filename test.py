print("Hello World")

capitals={'usa':'DC','sweden':'stockholm','norway':'oslo'}

print(capitals.get("norway"))

capitals['india']='delhi'

print(capitals)

print(capitals.keys())

for i in capitals:
    print(i,capitals[i])


for key,value in capitals.items():
    print(key,value)