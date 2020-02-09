from tkinter import *
from subprocess import Popen
import sys
def clicked():
	Popen(['python3', 'main.py'])
root = Tk()
root.title("Голосовой ассистент")
root.geometry("800x500+600+500")
root.resizable(width=False, height=False)
root.configure(background='#97c7f1') 
btn1 = Button(text="Запустить ассистента", background="#0000FF",  padx="300",foreground="#fff", pady="8", font="12", width=20, command=clicked)
btn1.pack(side=BOTTOM)

label = Label(text="Добро пожаловать!", font="12", pady="8", background="blue")
label.pack()

root.mainloop()
