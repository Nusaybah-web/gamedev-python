import pgzrun,random

WIDTH=600
HEIGHT=400

bad=["battery","bag","bottle","chips"]

levels=10

win=False

loose=False

items=[]

def draw():
    screen.blit("hand",(0,0))
    if win:
        screen.fill("green")
        screen.draw.text("YOU WIN!!!",center=(605,450),Fontsize=400)
    elif loose:
        screen.fill("green")
        screen.draw.text("you loose",center=(605,450),Fontsize=400)
    else:
        for i in items:
            i.draw()

def rain(extra):
    itemslist=populate(extra)
    images=things(itemslist)
    layout(images)
    animate(images)
    return images

def populate(extra):
    itemslist=["paper"]
    for i in range(extra):
        z=random.choice(bad)
        itemslist.append(z)
    return itemslist

def things(itemslist):
    images=[]
    for i in itemslist:
        actors=Actor(i)
        images.append(actors)
    return images

def layout(num):
    numgaps=len(num)+1
    gapsize=WIDTH/numgaps
    random.shuffle(num)
    for i,j in enumerate(num,1):
        x=gapsize*i
        j.x=x



