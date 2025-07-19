names=["anna","cindy","ella"]

print(names[2])

metrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(metrix[2][0])

print(len(metrix))#rows
print(len(metrix[0]))

for i in metrix:
    print(i)
for i in range(len(metrix)):
    print()
    for j in range(len(metrix[1])):
        print(metrix[i][j],end=" ")

#input

'''rows=int(input("how many rows should the list have: "))
collums=int(input("how many rowscollums should each row have: "))

list=[]

for i in range(rows):
    temp=[]
    for j in range(collums):
        num=int(input("please enter a number"))
        temp.append(num)
    list.append(temp)

print(list)
'''

#math

l1=[[1,2],[3,4]]
l2=[[5,6],[7,8]]
results=[[0,0],[0,0]]

for i in range(len(l1)):
    for j in range(len(l1[0])):
        results[i][j]=l1[i][j]+l2[i][j]
print(results)