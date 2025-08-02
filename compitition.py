'''groupname=("tigers","lions","jagwars","cheetas","panthers")

info=(('4','3','4','3','5'),('12.04.24','03.10.25','04.25.25','04.30.25','05.27.25'),('purr art gailery','kitten theater','meow golf corse','cat basketball course','kitty fotball stadume'),('silver','bronze','silver','gold','gold'))

size,date,venue,medal=info

tigers,lions,jagwars,cheetas,panthers=1,2,3,4,5

team=input("which team do you want to know about: ")

teaminfo=input("what do you want to know about: ")

print(team[teaminfo])'''

group=[]

for i in range(2):
    print(f"please enter the info for group {i+1}")
    groupname=input("please enter the groupname")
    size=input("please enter the size of the group")
    date=input("please enter the date of the next compitition")
    venue=input("please enter venue")
    medal=input("please enter the type of medal they won last time")
    grouprecord=(groupname,size,date,venue,medal)
    group.append(grouprecord)

for i,j in enumerate(group,1):
    print(i,j)
