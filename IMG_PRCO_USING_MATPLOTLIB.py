import tkinter as tk

from tkinter import *
from tkinter.ttk import *
import pandas as pd
from sqlalchemy import create_engine
import tkinter.ttk as ttk



window = tk.Tk()
greeting = tk.Label(text="SUP")
greeting.pack()
window.mainloop()


window = tk.Tk()
label = tk.Label(text="yipeeee")
label.pack()
window.mainloop()
tk.Label()
ttk.Label()
Label()
Text()
label = tk.Label(text="Hello, Tkinter")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label = tk.Label(text="Hello, Tkinter", background="#34A2FE")



#task 1
window = tk.Tk()    
window.title("Yelllo")
window.mainloop()

#Task 2 
greeting=tk.Label(text="Hola visito!")
greeting.pack()
greeting.mainloop()

#task 3 
Lable =tk.Label(
    text="SHAZAAM",
    fg="white",
    bg="red",
)
Lable.pack()
Lable.mainloop()

#Task 4 
Lable =tk.Label(
    text="KABOOOM",
    fg="white",
    bg="red",
    width=40,
    height=10    
)
Lable.pack()
Lable.mainloop()

#Task 5
button =tk.Button(
    text="Hit me",
    width=50,
    height=20,
    bg="red",
    fg="green",
)
button.pack()
button.mainloop()

#POST LAB
root = tk.Tk()
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Del First Char", command=lambda: entry.delete(0)).pack()
tk.Button(root, text="Del First 4", command=lambda: entry.delete(0, 4)).pack()  
tk.Button(root, text="Remove All", command=lambda: entry.delete(0, tk.END)).pack()
tk.Button(root, text="Insert Text", command=lambda: entry.insert(0, "HEHEHE")).pack()

root.mainloop()

