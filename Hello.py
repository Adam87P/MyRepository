print=("Hello there!")
	
from tkinter import *
 
window = Tk()
 
window.title("Welcome to Adam app")
 
window.geometry('450x250')
 
lbl = Label(window, text="Hello world!", font=("Arial", 28))
 
lbl.grid(column=0, row=0)
 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
    import sys
sys.path.append(C:\Users\Szczupak\Desktop\Python)
import Quiz

btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
btn = Button(window, text="Mini quiz", command=clicked)
btn.grid(column=2, row=0)


lbl = Label(window, text="My name is Adam Pietrasik and I would like to become tester.")
lbl.grid(column=0, row=2)
lbl = Label(window, text="Although I have no technical background...")
lbl.grid(column=0, row=3)
lbl = Label(window, text="and have no professional experience...")
lbl.grid(column=0, row=4)
lbl = Label(window, text="I am capable of learning new things!")
lbl.grid(column=0, row=5)
lbl = Label(window, text="Like Python! (which is really likable language)")
lbl.grid(column=0, row=6)
lbl = Label(window, text="Please, find a moment for my small quiz.")
lbl.grid(column=0, row=7)
lbl = Label(window, text="Thank you!")
lbl.grid(column=0, row=8)
lbl = Label(window, text="You can find more about me on my LinkedIn profile.")
lbl.grid(column=0, row=9)


import webbrowser


def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="LinkedIn", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/adam-pietrasik-8517a1107/"))
