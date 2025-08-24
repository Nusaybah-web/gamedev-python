import pgzrun,random


WIDTH=1000
HEIGHT=750

good=Actor("goodship")
good.pos=(600,650)

ani=[]

bees=[]

images=[]

lazers=[]

loose=False

win=False

def draw():
    screen.fill("dark blue")
    good.draw()
    for i in bees:
        i.draw()

    for l in lazers:
        screen.draw.line((l.x,l.y),(l.x,l.y-15),"white")

    if win:
        screen.draw.text("YOU WIN!!!!!!!!",center=(500,375),fontsize=100)
    elif loose:
        screen.draw.text("you loose",center=(500,375),fontsize=100)



for i in range(10):
    bad=Actor("badship")
    bad.pos=random.randint(50,950),random.randint(0,0)
    bees.append(bad)



def anime(bees):
    global ani
    for i in bees:
        duration=random.randint(8,10)
        i.anchor=("center","bottom")
        animate(i,duration=duration,on_finished=gameover,y=HEIGHT)
        

def update():
    if loose:
        return

    if keyboard.left:
        good.x-=6
    elif keyboard.right:
        good.x+=6

    for l in lazers[:]:
        l.y-=10
        if l.y<0:
            lazers.remove(l)
        else:
            for enemies in bees:
                if enemies.collidepoint(l.x,l.y):
                    bees.remove(enemies)
                    if l in lazers:
                        lazers.remove(l)

def gameover():
    global loose
    loose=True

def shoot():
    laser=Actor("badship")
    laser.x,laser.y=good.x,good.y
    lazers.append(laser)

anime(bees)



clock.schedule_interval(shoot,0.2)

pgzrun.go()