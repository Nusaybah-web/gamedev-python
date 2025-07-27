import random,pgzrun
from time import time


WIDTH=500
HEIGHT=400

sats=[]
lines=[]

start_time=time()

for i in range(8):
    satelite=Actor("satelite")
    satelite.pos=random.randint(20,480),random.randint(20,380)
    sats.append(satelite)
    


def draw():
    global lines
    desplay=time()-start_time
    screen.blit("space",(0,0))
    num=1
    for i in sats:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+17))
        num+=1
    screen.draw.text(str(round(desplay,1)),(30,30))
    for i in lines:
        screen.draw.line(i[0],i[1],"white")


def update():
    pass

next_satelite=0
def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite<8:
        if sats[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((sats[next_satelite-1].pos,sats[next_satelite].pos))
            next_satelite+=1
        else:
            lines=[]
            next_satelite=0
                


pgzrun.go()