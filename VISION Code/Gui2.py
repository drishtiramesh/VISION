from tkinter import *
import sys
import os
from tkinter.filedialog import askopenfilename
 
window = Tk()

OPTIONS = [
    "All",
"Dhawal Negi",
"Drishti R M",
"Sai Krishnan",
"Asad Ansari",
"Piyali Pal"
] 
window.title("Welcome to the VISION")

variable = StringVar(window)
variable.set(OPTIONS[0])

w = OptionMenu(window, variable, *OPTIONS)
w.grid(column=0 , row=0)

window.geometry('350x200')
lb1 = Label(window, text="Initialise Dataset")
lb2 = Label(window, text="Recognise Faces in Images")
lb3 = Label(window, text="See for a face using Webcam")
lb4 = Label(window, text="Search for the face using Drone camera")


lb1.grid(column=0, row=1)
lb2.grid(column=0, row=2)
lb3.grid(column=0, row=3)
lb4.grid(column=0, row=4)

def clicked1():
 
    os.system('Initialiser.py')
   
def clicked2():
 
    os.system('Recog_from_Images.py')

def clicked3():
 
    os.system('Recog_from_Webcam.py')

def clicked4():
 
    os.system('Recog_from_Drone_Camera.py')

def clicked5():

     fp=open("name.txt","w")
     fp.write(variable.get())
         

btn1 = Button(window, text="Click Me", command=clicked1)
btn2 = Button(window, text="Click Me", command=clicked2)
btn3 = Button(window, text="Click Me", command=clicked3)
btn4 = Button(window, text="Click Me", command=clicked4)
btn5 = Button(window, text="Confirm", command=clicked5)
 
btn1.grid(column=1, row=1)
btn5.grid(column=1, row=0)
btn2.grid(column=1, row=2)
btn3.grid(column=1, row=3)
btn4.grid(column=1, row=4)

 
window.mainloop()
