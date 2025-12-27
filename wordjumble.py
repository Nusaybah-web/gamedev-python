from tkinter import *
import random

score=0

words=["apple","orange","banana","sweden","school","paper","words","brain","fire","cake"]
letters=[]
for i in words:
    letters.append(" ".join(random.sample(i,len(i))))


r=random.randrange(0,len(letters),1)

def reset():
    global r,letters,words
    r=random.randrange(0,len(letters),1)
    lable2.config(text=letters[r])
    entry.delete(0,END)


def default():
    global r,letters,lable2
    lable2.config(text=letters[r])

def pl():
    global r,score,letters,lable3
    lable2.config(text=letters[r])
    answer=entry.get()
    if answer==words[r]:
        score+=1
    
    lable3.config(text="Score: "+str(score))
    reset() 




#desighn 

root=Tk()

root.configure(bg="black")

lable1=Label(root,text="WORD JUMBLE GAME",font=("ariel",15,"normal"),bg="black",fg="white")
lable2=Label(root,text=" ",font=("ariel",10,"normal"),bg="black",fg="white")
lable1.pack(pady=10,padx=15)
lable2.pack(pady=10)

entry=Entry(root,font=("ariel",10,"normal"),width=10)
entry.pack(pady=10)

button1=Button(root,text="check",command=pl)
button2=Button(root,text="reset")
button1.pack(pady=5)
button2.pack(pady=5)


lable3=Label(root,text=f"Score: 0",font=("ariel",15,"normal"),bg="black",fg="white")
lable3.pack(anchor=W)

default()

mainloop()