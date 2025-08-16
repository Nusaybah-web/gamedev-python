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

cq=0
tq=0

sbm=f"welcome to kahoot, you are currently on question number {cq}/{tq}"

info=[]

def draw():
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
    
    
questions()

lines=readquestions()

print(lines)














pgzrun.go()