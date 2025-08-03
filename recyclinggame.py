import pgzrun,random

WIDTH=1210
HEIGHT=900

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




