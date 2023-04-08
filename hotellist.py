from tkinter import ttk
from random import randint, choice
from tkinter import*
from PIL import Image, ImageTk
import re


def main_screen(root): 

    global screen

    screen = root
    screen.geometry("1500x800")
    screen.configure(bg="#d7dae2")
    screen.title("Hotel List")


    #hotel1
    hotel1=Image.open('panpacific.png')
    hotel1=hotel1.resize((200,400),Image.ANTIALIAS)
    photo_logo=ImageTk.PhotoImage(hotel1)

    title_frame=Frame(root,bd=2,relief=RIDGE)
    title_frame.place(x=450,y=28,width=550,height=82)

    title_lbl=Label(title_frame,image=photo_logo,compound=LEFT,text='Hotel Recommendation Form', font=('times new roman',28,'bold'),fg='darkblue')
    title_lbl.place(x=10,y=15)

    #hotel2

    scrollbar=ttk.Scrollbar(screen,orient='vertical')
    scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')
 
    screen.bind('<MouseWheel>', lambda event: screen.yview_scroll(20,"units"))
    
    screen.mainloop()

root = Tk()
main_screen(root)

