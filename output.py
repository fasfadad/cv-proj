from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import re

def program():
    ws = Tk()
    ws.geometry('400x300')
    ws.title('PythonGuides')
    ws['bg']='#ffbf00'

<<<<<<< HEAD:page2.py
    f = ("Times bold", 14)
    
    def nextPage():
        ws.destroy()
        import registration

    def prevPage():
        ws.destroy()
        import registration
=======
f = ("Times bold", 14)
 
def nextPage():
    ws.destroy()
    import input

def prevPage():
    ws.destroy()
    import input
>>>>>>> 9b473125ddfc9f00d29b58ca76f219f89f055c66:output.py

    Label(
        ws,
        text="This is Second page",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(expand=True, fill=BOTH)

    Button(
        ws, 
        text="Previous Page", 
        font=f,
        command=nextPage
        ).pack(fill=X, expand=TRUE, side=LEFT)
    Button(
        ws, 
        text="Next Page", 
        font=f,
        command=prevPage
        ).pack(fill=X, expand=TRUE, side=LEFT)

    ws.mainloop()
    
program()
