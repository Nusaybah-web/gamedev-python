import pgzrun,random

TITLE="catch the alien"

WIDTH=600
HEIGHT=500

alien=Actor("alien")
alien.pos=300,250

text="game start"


def draw():
    screen.fill("dark blue")
    alien.draw()
    screen.draw.text(text,(20,20),fontsize=30)

def on_mouse_down(pos):
    global text
    if alien.collidepoint(pos):
        alien.x=random.randint(50,550)
        alien.y=random.randint(50,450)
        text="good shot"
        sounds.eep.play()
    else:
        #alien.x=random.randint(50,550)
        #alien.y=random.randint(50,450)
        text="almost"

def update():
    alien.x+=3
    if alien.x>=600:
        alien.x=0
        alien.y=random.randint(5,450)


pgzrun.go()