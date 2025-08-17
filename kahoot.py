import pgzrun

TITLE="welcome to kahoot but from temu"

WIDTH=800
HEIGHT=600

sb=Rect(0,50,800,50)
q=Rect(20,120,600,130)
a1=Rect(20,270,290,130)
a2=Rect(330,270,290,130)
a3=Rect(20,420,290,130)
a4=Rect(330,420,290,130)
timer=Rect(640,120,140,130)
skip=Rect(640,270,140,280)

answers=[a1,a2,a3,a4]


cq=0
tq=0




info=[]

time=10

finished=False
s=0

def draw():
    global cq,tq
    sbm=f"welcome to kahoot, you are currently on question number {cq}/{tq}"
    screen.fill("black")
    screen.draw.filled_rect(sb,"black")
    screen.draw.filled_rect(q,"red")
    screen.draw.filled_rect(a1,"red")
    screen.draw.filled_rect(a2,"red")
    screen.draw.filled_rect(a3,"red")
    screen.draw.filled_rect(a4,"red")
    screen.draw.filled_rect(timer,"red")
    screen.draw.filled_rect(skip,"red")
    screen.draw.textbox(sbm,sb,color="white")
    screen.draw.textbox(lines[0],q,color="white")
    
    for i,j in enumerate(answers,1):
        screen.draw.textbox(lines[i].strip(),j,color="white")

    screen.draw.textbox("skip",skip,color="white")
    screen.draw.textbox(str(time),timer,color="white")



def update():
    sb.x-=2
    if sb.right==0:
        sb.x=800

def questions():
    global tq
    with open("questions.txt") as file:
        for i in file:
            info.append(i)
            tq+=1

def readquestions():
    global cq
    cq+=1
    return info.pop(0).split("|")


def timer2():
    global time
    if time:
        time-=1
    else:
        gameover()

def gameover():
    global finished,lines,time
    finished=True
    lose=f"game over, you have {s} correct"
    lines=[lose,"-","-","-","-",5]
    time=0

def ca():
    global s,time,lines
    s+=1
    if info:
        lines=readquestions()
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

def skip2():
    global time,lines
    if info and not finished:
        lines=readquestions()
        time=10
    else:
        gameover()


questions()   

lines=readquestions()

print(lines)

clock.schedule_interval(timer2,1)


pgzrun.go()