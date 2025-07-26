from random import randint

print("welcome to the tresure game, where you will guess where the treasure is buried in this grid")

#grid=[["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"]]

grid=[["-" for j in range(5)]for i in range(5)]


for i in grid:
    for j in grid[0]:
        print(j,end=" ")
    print()

tresurex=randint(0,4)
tresurey=randint(0,4)

while True:
    x=int(input("please enter which row you think the treasur is buried (0-4): "))
    y=int(input("please enter which collum you think the treasur is buried (0-4): "))

    if tresurex>x:
        print("go down")
    elif tresurex<x:
        print("go up")
    elif tresurey>y:
        print("go right")
    elif tresurey<y:
        print("go left")
    else:
        print("you found the treasure!!!")
        break
        
