import pgzrun,random

WIDTH=600
HEIGHT=400

bad=["battery","bag","bottle","chips"]

ani=[]

cl=1

levels=6

win=False

loose=False

items=[]

def draw():
    screen.blit("hand",(0,0))
    if win:
        screen.fill("green")
        screen.draw.text("YOU WIN!!!",center=(300,200),fontsize=40)
    elif loose:
        screen.fill("red")
        screen.draw.text("you loose",center=(300,200),fontsize=40)
    else:
        for i in items:
            i.draw()

def update():
    global items
    if len(items)==0:
        items=rain(cl)

def rain(extra):
    il=populate(extra)
    images=things(il)
    layout(images)
    anime(images)
    return images

def populate(extra):
    il=["paper"]
    for i in range(extra):
        z=random.choice(bad)
        il.append(z)
    return il

def things(il):
    images=[]
    for i in il:
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

def anime(images):
    for i in images:
        duration=10-cl
        i.anchor=("center","bottom")
        copyanime=animate(i,duration=duration,on_finished=gameover,y=HEIGHT)
        ani.append(copyanime)

def gameover():
    global loose
    loose=True

def complete():
    global items,ani,cl
    stop(ani)
    if cl==levels:
        win=True
    else:
        cl+=1
        items=[]
        ani=[]



def on_mouse_down(pos):
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                complete()
            else:
                gameover()

def stop(anim):
    for i in anim:
        if i.running:
            i.stop()


pgzrun.go()
                










