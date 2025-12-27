from tkinter import *
from gtts import gTTS
import os

root=Tk()

def sound():
    s=gTTS(text=entry.get(),lang="en")
    s.save("pygamesound.wav")
    os.system("pygamesound.wav")


entry=Entry(root,width=40)
entry.pack(pady=10,padx=10)

button=Button(root,text="submit",command=sound)
button.pack(pady=10,padx=10)

mainloop()

