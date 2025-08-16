import pgzrun,random

WIDTH=800
HEIGHT=600

fake=("blue_star","green_star","orange_star","purple_star","red_star")

loose=False
win=False

levils=8
cl=1

star=[]

ani=[]

def draw():
    screen.blit("space",(0,0))
    if win:
        screen.draw.text("YOU WIN!!!",center=(400,300),fontsize=80)
    elif loose:
        screen.draw.text("You loose...",center=(400,300),fontsize=80)
    else:
        for i in star:
            i.draw()

def update():
    global star
    if len(star)==0:
        star=mother(cl)

def mother(extra):
    stars=a(extra)
    visual=b(stars)
    layout(visual)
    anime(visual)
    return visual


def a(extra):
    stars=["white_star"]
    for i in range(extra):
        choice=random.choice(fake)
        stars.append(choice)
    return(stars)

def b(stars):
    visual=[]
    for i in stars:
        actor=Actor(i)
        visual.append(actor)
    return(visual)

def layout(num):
    gap=len(num)+1
    gapsize=WIDTH/gap
    random.shuffle(num)
    for i,j in enumerate(num,1):
        x=gapsize*i
        j.x=x

def anime(visual):
    for i in visual:
        duration=10-cl
        i.anchor=("center","bottom")
        copyanime=animate(i,duration=duration,on_finished=gameover,y=HEIGHT)
        ani.append(copyanime)

def gameover():
    global loose
    loose=True

def complete():
    global star,ani,cl,win
    stop(ani)
    if cl==levils:
        win=True
    else:
        cl+=1
        star=[]
        ani=[]

def stop(anim):
    for i in anim:
        if i.running:
            i.stop()

def on_mouse_down(pos):
    for i in star:
        if i.collidepoint(pos):
            if "white_star" in i.image:
                complete()
            else:
                gameover()

pgzrun.go()









