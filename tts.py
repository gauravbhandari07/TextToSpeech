from tkinter import *
from PIL import Image, ImageTk
import pyttsx3 as pt

def speaks():
    text_speech = pt.init();

    text_speech.say(textvalue.get());
    text_speech.runAndWait();

root= Tk()

root.geometry("1000x600")
root.minsize(100,60)
root.title("Text to Speech")

lbl1=Label(text="Text to Speech Converter",fg="Blue", font=("black diamond regular", 20, "bold"))
lbl1.grid(row=0,column=5)

text= Label(root, text="enter something")
text.grid(row=1,column=1)
textval= StringVar()
textvalue= Entry(root, textvariable= textval)
textvalue.grid(row=2,column=1)

b1=Button(fg="Blue", text="speak", command=speaks)
b1.grid(row=2,column=2)


root.mainloop()
