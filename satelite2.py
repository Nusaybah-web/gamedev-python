import random,pgzrun

WIDTH=500
HEIGHT=400

sats=[]
lines=[]

timer=False

for i in range(8):
    satelite=Actor("satelite")
    satelite.pos=random.randint(30,460),random.randint(30,360)
    sats.append(satelite)
    


def draw():
    global lines
    if timer==False:
        screen.blit("space",(0,0))
        num=1
        for i in sats:
            i.draw()
            screen.draw.text(str(num),(i.pos[0],i.pos[1]+17))
            num+=1
        for i in lines:
            screen.draw.line(i[0],i[1],"white")
    elif next_satelite==7:
        screen.draw.text("game over",center=(250,100),fontsize=100)
        if next_satelite<8:
            screen.draw.text("you loose",center=(250,200),fontsize=50)
        else:
            screen.draw.text("you win",center=(250,200),fontsize=50)




def update():
        pass


next_satelite=0
def on_mouse_down(pos):
    global next_satelite,lines,t
    if next_satelite<8:
        if sats[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((sats[next_satelite-1].pos,sats[next_satelite].pos))
            next_satelite+=1
        else:
            lines=[]
            next_satelite=0

def finished():
    global timer
    timer=True

clock.schedule(finished,15)

                

pgzrun.go()