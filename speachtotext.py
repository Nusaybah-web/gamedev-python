from tkinter import *
import speech_recognition as sr
import threading
from tkinter.filedialog import *

isrecording=False

def listen():
    global isrecording
    l=sr.Recognizer()
    with sr.Microphone() as source:
        textbox.insert(END,"started listening \n")
        textbox.see(END)
        while isrecording:
            try:
                print("listening")
                audio=l.listen(source,timeout=5)
                text=l.recognize_google(audio)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                text="unrecognised speech"
            except sr.RequestError:
                text="apierror"
            textbox.insert(END,text+"\n")
            textbox.see(END)
        
def startrecording():
    global isrecording
    if not isrecording:
        isrecording=True
        threading.Thread(target=listen,daemon=True).start()


def stoprecording():
    global isrecording
    isrecording=False
    textbox.insert(END,"((stopped recording))")

def save():
    file=asksaveasfile()
    if file:
        print(textbox.get(1.0,END),file=file)

    


root=Tk()

lable=Label(root,text="Speech to text",font=("calibri",30,"normal"))
lable.grid(row=0,column=0,columnspan=2)

button1=Button(root,text="start recording",command=startrecording)
button2=Button(root,text="stop recording",command=stoprecording)
button3=Button(root,text="save text",command=save)

button1.grid(row=1,column=0)
button2.grid(row=2,column=0)
button3.grid(row=3,column=0)

textbox=Text(root,height=30,width=50)
textbox.grid(row=1,column=1,rowspan=3)

mainloop()