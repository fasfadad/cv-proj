from tkinter import ttk
from random import randint, choice
from tkinter import*
from PIL import Image, ImageTk
import re


def main_screen(root): 

    global screen

    screen = root
    screen.geometry("900x800")
    screen.configure(bg="#d7dae2")
    screen.title("Hotel List")


    #hotel1
    hotel1=Image.open('panpacific.png')
    hotel1=hotel1.resize((400,260),Image.ANTIALIAS)
    photo_logo1=ImageTk.PhotoImage(hotel1)

    hotel1_frame=Frame(root,bd=5,relief=RIDGE)
    hotel1_frame.place(x=30,y=28,width=820,height=4000
)
    placement1=Label(hotel1_frame,image=photo_logo1,compound=LEFT)
    placement1.place(x=10,y=15)

    hotelname=Label(hotel1_frame,text='Pan Pacific Singapore', font=('times new roman',24,'bold'),fg='darkblue')
    hotelname.grid(row=0,column=0,padx=430,pady=20,sticky=W)
    info=Label(hotel1_frame,text='Price: $282', font=('times new roman',12,'bold'))
    info.grid(row=1,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel1_frame,text='Hotel Rating: 5 Star', font=('times new roman',12,'bold'))
    info.grid(row=2,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel1_frame,text='Breakfast Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=3,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel1_frame,text='Shuttle Service Availability: No', font=('times new roman',12,'bold'))
    info.grid(row=4,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel1_frame,text='Spa Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=5,column=0,padx=430,pady=5,sticky=W)


    #hotel2
    hotel2=Image.open('parkroyal.png')
    hotel2=hotel2.resize((400,260),Image.ANTIALIAS)
    photo_logo2=ImageTk.PhotoImage(hotel2)

    hotel2_frame=Frame(root,bd=5,relief=RIDGE)
    hotel2_frame.place(x=30,y=325,width=820,height=315)

    placement2=Label(hotel2_frame,image=photo_logo2,compound=LEFT)
    placement2.place(x=10,y=15)


    hotelname=Label(hotel2_frame,text='Pan Pacific Singapore', font=('times new roman',24,'bold'),fg='darkblue')
    hotelname.grid(row=0,column=0,padx=430,pady=20,sticky=W)
    info=Label(hotel2_frame,text='Price: $282', font=('times new roman',12,'bold'))
    info.grid(row=1,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel2_frame,text='Hotel Rating: 5 Star', font=('times new roman',12,'bold'))
    info.grid(row=2,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel2_frame,text='Breakfast Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=3,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel2_frame,text='Shuttle Service Availability: No', font=('times new roman',12,'bold'))
    info.grid(row=4,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel2_frame,text='Spa Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=5,column=0,padx=430,pady=5,sticky=W)

    #hotel3
    hotel3=Image.open('ritzcarlton.png')
    hotel3=hotel3.resize((400,260),Image.ANTIALIAS)
    photo_logo3=ImageTk.PhotoImage(hotel3)

    hotel3_frame=Frame(root,bd=5,relief=RIDGE)
    hotel3_frame.place(x=30,y=600,width=820,height=305)

    placement3=Label(hotel3_frame,image=photo_logo3,compound=LEFT)
    placement3.place(x=10,y=15)


    hotelname=Label(hotel3_frame,text='Pan Pacific Singapore', font=('times new roman',24,'bold'),fg='darkblue')
    hotelname.grid(row=0,column=0,padx=430,pady=20,sticky=W)
    info=Label(hotel3_frame,text='Price: $282', font=('times new roman',12,'bold'))
    info.grid(row=1,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel3_frame,text='Hotel Rating: 5 Star', font=('times new roman',12,'bold'))
    info.grid(row=2,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel3_frame,text='Breakfast Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=3,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel3_frame,text='Shuttle Service Availability: No', font=('times new roman',12,'bold'))
    info.grid(row=4,column=0,padx=430,pady=5,sticky=W)
    info=Label(hotel3_frame,text='Spa Availability: Yes', font=('times new roman',12,'bold'))
    info.grid(row=5,column=0,padx=430,pady=5,sticky=W)











    scrollbar=ttk.Scrollbar(screen,orient='vertical')
    scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')
 
    screen.bind('<MouseWheel>', lambda event: screen.yview_scroll(20,"units"))
    
    screen.mainloop()

root = Tk()
main_screen(root)

