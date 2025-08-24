import pgzrun,random

TITLE="Kahoot(temu vreson)"

HEIGHT=530
WIDTH=800

q=Rect(20,20,600,150)
a1=Rect(20,190,290,150)
a2=Rect(330,190,290,150)
a3=Rect(20,360,290,150)
a4=Rect(330,360,290,150)
timer=Rect(640,20,140,150)
skip=Rect(640,190,140,320)

cq=0
tq=0

info=[]

finished=False

score=0

answers=[a1,a2,a3,a4]

time=10


def draw():
    screen.fill("white")
    screen.draw.filled_rect(q,"red")
    screen.draw.filled_rect(a1,"red")
    screen.draw.filled_rect(a2,"red")
    screen.draw.filled_rect(a3,"red")
    screen.draw.filled_rect(a4,"red")
    screen.draw.filled_rect(timer,"red")
    screen.draw.filled_rect(skip,"red")
    screen.draw.textbox(lines[0],q,color="white")
    for i,j in enumerate(answers,1):
        screen.draw.textbox(lines[i].strip(),j,color="white")
    screen.draw.textbox("skip",skip,color="white")
    screen.draw.textbox(str(time),timer,color="white")



def update():
    pass

def timer2():
    global time
    if time:
        time-=1
    else:
        gameover()


def questions():
    global tq
    with open("questions.txt") as file:
        for i in file:
            info.append(i)
            tq+=1

def rq():
    global cq
    cq+=1
    
    choice=random.randint(0,len(info)-1)
    return info.pop(choice).split("|")

def ca():
    global score,time,lines
    score+=1
    if info:
        lines=rq()
        time=10
    else:
        gameover()

def gameover():
    global finished,lines,time
    finished=True
    lose=f"game over, you have {score} correct"
    lines=[lose,"-","-","-","-",5]
    time=0

def skip2():
    global time,lines
    if info and not finished:
        lines=rq()
        time=10
    else:
        gameover()

def on_mouse_down(pos):
    for i,j in enumerate(answers,1):
        if j.collidepoint(pos):
            if i is int(lines[5]):
                ca()
            else:
                gameover()

    if skip.collidepoint(pos):
        skip2()






questions()

lines=rq()

clock.schedule_interval(timer2,1)

pgzrun.go()