import pgzrun,random

WIDTH=400
HEIGHT=400



'''def draw():
    w=400
    h=200
    r=255
    g=0
    b=random.randint(0,255)
    screen.fill((255,255,255))
    for i in range(20):
        obg=Rect(0,200,w,h)
        obg.center=200,200
        screen.draw.rect(obg,(r,g,b))
        w-=10
        h+=10
        r-=10
        g+=10'''
    
def draw():
    obg=Rect(0,200,200,200)
    obg.center=200,200
    screen.draw.filled_rect(obg,(255,255,255))
    screen.draw.filled_circle((200,200),100,"black")
    screen.draw.line((100,200),(300,200),"white")

pgzrun.go()
