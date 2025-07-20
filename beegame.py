import pgzrun,random

WIDTH=600
HEIGHT=500

bee=Actor("bee")
bee.pos=300,250
flower=Actor("flower")
flower.pos=300,300

score=0

gameover=False

def draw():
    global score
    screen.blit("grassfeild",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(f"score: {score}",color="blue",topleft=(20,20),fontsize=30)
    if gameover:
        screen.fill("green")
        screen.draw.text(f"Times up! \n your score is: {score}",color="white",center=(300,250),fontsize=50)


def update():
    global score
    if keyboard.left:
        bee.x-=4
    elif keyboard.right:
        bee.x+=4
    elif keyboard.up:
        bee.y-=4
    elif  keyboard.down:
        bee.y+=4
    if bee.colliderect(flower):
        score+=10
        flower.pos=random.randint(20,290),random.randint(20,290)

def finished():
    global gameover
    gameover=True

clock.schedule(finished,20)


pgzrun.go()