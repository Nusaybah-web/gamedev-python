import random

grades=[]

l1=[]
l2=[]
l3=[]

for i in range(20):
    num=random.randint(0,100)
    if num<=30:
        l1.append(num)
    elif num>30 and num<70:
        l2.append(num)
    elif num>=70:
        l3.append(num)

grades.append(l1)
grades.append(l2)
grades.append(l3)

for i in grades:
    print(i)
    