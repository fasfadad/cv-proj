from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import re

def mainprogram():

    def destroyandimport():
            root.destroy()
            program()
            
    class Register():

<<<<<<< HEAD:registration.py
        def __str__(self):
             return self.location_var.get()
        
        def validation(self):
            if self.location_var.get() == '':
                    messagebox.showerror('Error', 'Please select your Location', parent=self.root)
            elif self.hotel_rating_var.get() == 0 and self.location_var.get() != "":
                    messagebox.showerror('Error', 'Please select Hotel Rating', parent=self.root)
            else :
                destroyandimport()
                        
        def clearData(self):
            self.location_var.set("")
            self.hotel_rating_var.set(0)
            self.price.set(200)
            self.breakfast_var.set(-1)
            self.shuttlebus_var.set(-1)
            self.spa_var.set(-1)
=======
    def validation(self):
        if self.location_var.get() == '':
                messagebox.showerror('Error', 'Please select your Location', parent=self.root)
        elif self.hotel_rating_var.get() == 0 and self.location_var.get() != "":
                messagebox.showerror('Error', 'Please select Hotel Rating', parent=self.root)
        else:
            root.destroy()
            import output
                  
    def clearData(self):
        self.location_var.set("")
        self.hotel_rating_var.set(0)
        self.price.set(200)
        self.breakfast_var.set(-1)
        self.shuttlebus_var.set(-1)
        self.spa_var.set(-1)
>>>>>>> 9b473125ddfc9f00d29b58ca76f219f89f055c66:input.py

        def __init__(self,root):
            self.root=root
            self.root.title('Hotel Recommendation Page')
            self.root.geometry('1500x800')


            #Variables
            self.location_var=StringVar()
            self.hotel_rating_var=IntVar()
            self.breakfast_var=IntVar()
            self.shuttlebus_var=IntVar()
            self.price =IntVar()
            self.spa_var=IntVar()

            # initialize variable
            self.location_var.set("")
            self.hotel_rating_var.set(0)
            self.breakfast_var.set(-1)
            self.shuttlebus_var.set(-1)
            self.price.set(0)
            self.spa_var.set(-1)

            #Images
            self.bg=ImageTk.PhotoImage(file='bg.jpg')
            bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
            bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

            logo_img=Image.open('thumb2.png')
            logo_img=logo_img.resize((50,50),Image.ANTIALIAS)
            self.photo_logo=ImageTk.PhotoImage(logo_img)


            #Title1 frame
            title_frame=Frame(self.root,bd=2,relief=RIDGE)
            title_frame.place(x=450,y=28,width=550,height=82)

            title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='Hotel Recommendation Form', font=('times new roman',28,'bold'),fg='darkblue')
            title_lbl.place(x=10,y=15)


            #Information frame
            main_frame=Frame(self.root,bd=2,relief=RIDGE)
            main_frame.place(x=450,y=110,width=550,height=400)
            secondary_frame=Frame(self.root,bd=2,relief=RIDGE)
            secondary_frame.place(x=450,y=400,width=550,height=350)
            

            #Location
            mandatory_msg=Label(main_frame,text='Mandatory Questions*',font=('times new roman',10,'bold','underline'),fg='red')
            mandatory_msg.grid(row=0,column=0,padx=10,pady=10,sticky=W)

            location=Label(main_frame,text='Select Location:',font=('times new roman',14,'bold'))
            location.grid(row=1,column=0,padx=10,pady=10,sticky=W)

            list=['Marina Bay','Orchard Road','Chinatown','Sentosa','Clarke Quay']
            droplist=OptionMenu(main_frame, self.location_var, *list)
            droplist.config(width=20, font=('times new roman',14), bg='white')
            droplist.grid(row=1,column=1,padx=10,sticky=W)

            #Hotel Rating
            hotel_rating=Label(main_frame,text='Hotel Rating:',font=('times new roman',14,'bold'))
            hotel_rating.grid(row=2,column=0,padx=10,pady=10,sticky=W)

            rating_frame=Frame(main_frame)
            rating_frame.grid(row=2,column=1,columnspan=5,pady=25,sticky=W)

            radio_1 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=1, text='1', font=('times new roman', 14))
            radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            radio_2 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=2, text='2', font=('times new roman', 14))
            radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
            radio_3 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=3, text='3', font=('times new roman', 14))
            radio_3.grid(row=0, column=2, padx=10, pady=0, sticky=W)
            radio_4 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=4, text='4', font=('times new roman', 14))
            radio_4.grid(row=0, column=3, padx=10, pady=0, sticky=W)
            radio_5 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=5, text='5', font=('times new roman', 14))
            radio_5.grid(row=0, column=4, padx=10, pady=0, sticky=W)
            
            
            #Price
            price=Label(main_frame,text='Price Budget:',font=('times new roman',14,'bold'))
            price.grid(row=3,column=0,padx=10,pady=10,sticky=W)
            scale_frame=Frame(main_frame)
            scale_frame.grid(row=3, column=1, padx=10, pady=0, sticky=W)
            scale_min = Scale(scale_frame, from_=100, to=900, orient=HORIZONTAL, length=350, variable=self.price)
            scale_min.set(200)
            scale_min.pack(side=LEFT,ipady=8)
            

            #Breakfast
            optional_msg=Label(secondary_frame,text='Optional',font=('times new roman',10,'bold','underline'),fg='darkblue')
            optional_msg.grid(row=0,column=0,padx=10,pady=10,sticky=W)
            breakfast=Label(secondary_frame,text='Breakfast Availability:',font=('times new roman',14,'bold'))
            breakfast.grid(row=1,column=0,padx=10,pady=10,sticky=W)

            breakfast_frame=Frame(secondary_frame)
            breakfast_frame.grid(row=1,column=1,columnspan=5,pady=0,sticky=W)

            breakfast_radio_1 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='1', text='Yes', font=('times new roman', 14))
            breakfast_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            breakfast_radio_2 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='0', text='No', font=('times new roman', 14))
            breakfast_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
            

            #Shuttlebus Service
            shuttle_service=Label(secondary_frame,text='Shuttle Service Availability:',font=('times new roman',14,'bold'))
            shuttle_service.grid(row=2,column=0,padx=10,pady=10,sticky=W)

            shuttle_service_frame=Frame(secondary_frame)
            shuttle_service_frame.grid(row=2,column=1,columnspan=5,pady=0,sticky=W)

            shuttle_radio_1=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='1',text='Yes',font=('times new roman',14))
            shuttle_radio_1.grid(row=0,column=0,padx=10,pady=0,sticky=W)
            shuttle_radio_2=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='0',text='No',font=('times new roman',14))
            shuttle_radio_2.grid(row=0,column=1,padx=10,pady=0,sticky=W)

            #Spa
            spa=Label(secondary_frame,text='Spa Availability:',font=('times new roman',14,'bold'))
            spa.grid(row=3,column=0,padx=10,pady=10,sticky=W)

            spa_frame=Frame(secondary_frame)
            spa_frame.grid(row=3,column=1,columnspan=5,pady=0,sticky=W)
            spa_radio_1 = Radiobutton(spa_frame, variable=self.spa_var, value='1', text='Yes', font=('times new roman', 14))
            spa_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            spa_radio_2 = Radiobutton(spa_frame, variable=self.spa_var, value='0', text='No', font=('times new roman', 14))
            spa_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
        
            
            #Button Frame
            button_frame=Frame(secondary_frame,bd=2,relief=RIDGE)
            button_frame.place(x=34,y=250,width=480,height=70)

            
            search_button=Button(button_frame,text='Search',command=self.validation,font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='green',fg='white')
            search_button.grid(row=0,column=0,padx=23,pady=13,sticky=W)

            clear_button=Button(button_frame,text='Clear Data',font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='red',fg='white', command=self.clearData)
            clear_button.grid(row=0,column=2,padx=100,pady=13,sticky=W)

<<<<<<< HEAD:registration.py
    root=Tk()
    obj=Register(root)
    root.mainloop()
    m = obj
    print (m)

def program():
    def destroyandimport():
            root.destroy()
            mainprogram()
            
    class Register():

        def validation(self):
            if self.location_var.get() == '':
                    messagebox.showerror('Error', 'Please select your Location', parent=self.root)
            elif self.hotel_rating_var.get() == 0 and self.location_var.get() != "":
                    messagebox.showerror('Error', 'Please select Hotel Rating', parent=self.root)
            else :
                destroyandimport()
                        
        def clearData(self):
            self.location_var.set("")
            self.hotel_rating_var.set(0)
            self.price.set(200)
            self.breakfast_var.set(-1)
            self.shuttlebus_var.set(-1)
            self.spa_var.set(-1)

        def __init__(self,root):
            self.root=root
            self.root.title('Hotel Recommendation Page')
            self.root.geometry('1500x800')


            #Variables
            self.location_var=StringVar()
            self.hotel_rating_var=IntVar()
            self.breakfast_var=IntVar()
            self.shuttlebus_var=IntVar()
            self.price =IntVar()
            self.spa_var=IntVar()

            # initialize variable
            self.location_var.set("")
            self.hotel_rating_var.set(0)
            self.breakfast_var.set(-1)
            self.shuttlebus_var.set(-1)
            self.price.set(0)
            self.spa_var.set(-1)

            #Images
            self.bg=ImageTk.PhotoImage(file='bg.jpg')
            bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
            bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

            logo_img=Image.open('thumb2.png')
            logo_img=logo_img.resize((50,50),Image.ANTIALIAS)
            self.photo_logo=ImageTk.PhotoImage(logo_img)


            #Title1 frame
            title_frame=Frame(self.root,bd=2,relief=RIDGE)
            title_frame.place(x=450,y=28,width=550,height=82)

            title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='Hotel Recommendation Form', font=('times new roman',28,'bold'),fg='darkblue')
            title_lbl.place(x=10,y=15)


            #Information frame
            main_frame=Frame(self.root,bd=2,relief=RIDGE)
            main_frame.place(x=450,y=110,width=550,height=400)
            secondary_frame=Frame(self.root,bd=2,relief=RIDGE)
            secondary_frame.place(x=450,y=400,width=550,height=350)
            

            #Location
            mandatory_msg=Label(main_frame,text='Mandatory Fuck*',font=('times new roman',10,'bold','underline'),fg='red')
            mandatory_msg.grid(row=0,column=0,padx=10,pady=10,sticky=W)

            location=Label(main_frame,text='Select Location:',font=('times new roman',14,'bold'))
            location.grid(row=1,column=0,padx=10,pady=10,sticky=W)

            list=['Marina Bay','Orchard Road','Chinatown','Sentosa','Clarke Quay']
            droplist=OptionMenu(main_frame, self.location_var, *list)
            droplist.config(width=20, font=('times new roman',14), bg='white')
            droplist.grid(row=1,column=1,padx=10,sticky=W)

            #Hotel Rating
            hotel_rating=Label(main_frame,text='Hotel Rating:',font=('times new roman',14,'bold'))
            hotel_rating.grid(row=2,column=0,padx=10,pady=10,sticky=W)

            rating_frame=Frame(main_frame)
            rating_frame.grid(row=2,column=1,columnspan=5,pady=25,sticky=W)

            radio_1 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=1, text='1', font=('times new roman', 14))
            radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            radio_2 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=2, text='2', font=('times new roman', 14))
            radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
            radio_3 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=3, text='3', font=('times new roman', 14))
            radio_3.grid(row=0, column=2, padx=10, pady=0, sticky=W)
            radio_4 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=4, text='4', font=('times new roman', 14))
            radio_4.grid(row=0, column=3, padx=10, pady=0, sticky=W)
            radio_5 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=5, text='5', font=('times new roman', 14))
            radio_5.grid(row=0, column=4, padx=10, pady=0, sticky=W)
            
            
            #Price
            price=Label(main_frame,text='Price Budget:',font=('times new roman',14,'bold'))
            price.grid(row=3,column=0,padx=10,pady=10,sticky=W)
            scale_frame=Frame(main_frame)
            scale_frame.grid(row=3, column=1, padx=10, pady=0, sticky=W)
            scale_min = Scale(scale_frame, from_=100, to=900, orient=HORIZONTAL, length=350, variable=self.price)
            scale_min.set(200)
            scale_min.pack(side=LEFT,ipady=8)
            

            #Breakfast
            optional_msg=Label(secondary_frame,text='Optional',font=('times new roman',10,'bold','underline'),fg='darkblue')
            optional_msg.grid(row=0,column=0,padx=10,pady=10,sticky=W)
            breakfast=Label(secondary_frame,text='Breakfast Availability:',font=('times new roman',14,'bold'))
            breakfast.grid(row=1,column=0,padx=10,pady=10,sticky=W)

            breakfast_frame=Frame(secondary_frame)
            breakfast_frame.grid(row=1,column=1,columnspan=5,pady=0,sticky=W)

            breakfast_radio_1 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='1', text='Yes', font=('times new roman', 14))
            breakfast_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            breakfast_radio_2 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='0', text='No', font=('times new roman', 14))
            breakfast_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
            

            #Shuttlebus Service
            shuttle_service=Label(secondary_frame,text='Shuttle Service Availability:',font=('times new roman',14,'bold'))
            shuttle_service.grid(row=2,column=0,padx=10,pady=10,sticky=W)

            shuttle_service_frame=Frame(secondary_frame)
            shuttle_service_frame.grid(row=2,column=1,columnspan=5,pady=0,sticky=W)

            shuttle_radio_1=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='1',text='Yes',font=('times new roman',14))
            shuttle_radio_1.grid(row=0,column=0,padx=10,pady=0,sticky=W)
            shuttle_radio_2=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='0',text='No',font=('times new roman',14))
            shuttle_radio_2.grid(row=0,column=1,padx=10,pady=0,sticky=W)

            #Spa
            spa=Label(secondary_frame,text='Spa Availability:',font=('times new roman',14,'bold'))
            spa.grid(row=3,column=0,padx=10,pady=10,sticky=W)

            spa_frame=Frame(secondary_frame)
            spa_frame.grid(row=3,column=1,columnspan=5,pady=0,sticky=W)
            spa_radio_1 = Radiobutton(spa_frame, variable=self.spa_var, value='1', text='Yes', font=('times new roman', 14))
            spa_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
            spa_radio_2 = Radiobutton(spa_frame, variable=self.spa_var, value='0', text='No', font=('times new roman', 14))
            spa_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
        
            
            #Button Frame
            button_frame=Frame(secondary_frame,bd=2,relief=RIDGE)
            button_frame.place(x=34,y=250,width=480,height=70)

            
            search_button=Button(button_frame,text='Search',command=self.validation,font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='green',fg='white')
            search_button.grid(row=0,column=0,padx=23,pady=13,sticky=W)

            clear_button=Button(button_frame,text='Clear Data',font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='red',fg='white', command=self.clearData)
            clear_button.grid(row=0,column=2,padx=100,pady=13,sticky=W)

    root=Tk()
    obj=Register(root)
    root.mainloop()

    hotelmain = {
        1: {"name" : "Pan Pacific Singapore","location" : "Marina Bay","price" : 282,"hotelclass" : 5,"guestreview" : 8.8,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        2: {"name" : "PARKROYAL COLLECTION Marina Bay","location" : "Marina Bay","price" : 320,"hotelclass" : 5,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        3: {"name" : "Ritz-Carlton, Millenia Singapore","location" : "Marina Bay","price" : 444,"hotelclass" : 5,"guestreview" : 9.1,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        4: {"name" : "The Fullerton Hotel Singapore","location" : "Marina Bay","price" : 333,"hotelclass" : 5,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        5: {"name" : "Conrad Centennial Singapore","location" : "Marina Bay","price" : 294,"hotelclass" : 5,"guestreview" : 8.9,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        6: {"name" : "Fullerton Bay Hotel Singapore","location" : "Marina Bay","price" : 570,"hotelclass" : 5,"guestreview" : 9.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        7: {"name" : "Goodwood Park Hotel","location" : "Orchard Road","price" : 241,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        8: {"name" : "Hilton Singapore Orchard","location" : "Orchard Road","price" : 255,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 0},
        9: {"name" : "Singapore Marriott Tang Plaza Hotel","location" : "Orchard Road","price" : 294,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        10: {"name" : "Orchard Hotel Singapore","location" : "Orchard Road","price" : 173,"hotelclass" : 4,"guestreview" : 7.6,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        11: {"name" : "York Hotel","location" : "Orchard Road","price" : 167,"hotelclass" : 4,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        12: {"name" : "Royal Plaza on Scotts Hotel","location" : "Orchard Road","price" : 211,"hotelclass" : 5,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        13: {"name" : "Furama City Centre Hotel","location" : "Chinatown","price" : 143,"hotelclass" : 4,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        14: {"name" : "Dorsett Singapore","location" : "Chinatown","price" : 120,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        15: {"name" : "Butternut Tree Hotel","location" : "Chinatown","price" : 60,"hotelclass" : 2,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        16: {"name" : "The Scarlet Singapore","location" : "Chinatown","price" : 197,"hotelclass" : 4,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        17: {"name" : "Capri by Fraser, China Square","location" : "Chinatown","price" : 201,"hotelclass" : 4,"guestreview" : 8.6,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        18: {"name" : "W Singapore - Sentosa Cove","location" : "Sentosa","price" : 270,"hotelclass" : 5,"guestreview" : 8.6,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        19: {"name" : "ONE°15 Marina","location" : "Sentosa","price" : 239,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        20: {"name" : "Capella Singapore","location" : "Sentosa","price" : 853,"hotelclass" : 5,"guestreview" : 9.0,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        21: {"name" : "Resorts World Sentosa - Equarius Villas","location" : "Sentosa","price" : 330,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        22: {"name" : "Shangri-La Rasa, Sentosa","location" : "Sentosa","price" : 264,"hotelclass" : 5,"guestreview" : 8.9,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        23: {"name" : "Amara Sanctuary Resort Sentosa","location" : "Sentosa","price" : 211,"hotelclass" : 5,"guestreview" : 7.6,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        24: {"name" : "Park Regis Singapore","location" : "Clarke Quay","price" : 170,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        25: {"name" : "Holiday Inn Express Clarke Quay","location" : "Clarke Quay","price" : 168,"hotelclass" : 3,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        26: {"name" : "Paradox Singapore Merchant Court at Clarke Quay","location" : "Clarke Quay","price" : 192,"hotelclass" : 4,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        27: {"name" : "Studio M Hotel","location" : "Clarke Quay","price" : 128,"hotelclass" : 4,"guestreview" : 7.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        28: {"name" : "Peninsula Excelsior Hotel","location" : "Clarke Quay","price" : 172,"hotelclass" : 4,"guestreview" : 7.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        29: {"name" : "M Social Singapore","location" : "Clarke Quay","price" : 128,"hotelclass" : 4,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        30: {"name" : "D’Hotel Singapore","location" : "Tiong Bahru","price" : 121,"hotelclass" : 4,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        31: {"name" : "New Cape Inn","location" : "Tiong Bahru","price" : 75,"hotelclass" : 3,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        32: {"name" : "Nostalgia Hotel","location" : "Tiong Bahru","price" : 109,"hotelclass" : 4,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        33: {"name" : "Link Hotel Singapore","location" : "Tiong Bahru","price" : 118,"hotelclass" : 4,"guestreview" : 7.4,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 0},
        34: {"name" : "Coller Boutique Hostel","location" : "Tiong Bahru","price" : 46,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        35: {"name" : "Hotel 81 Osaka","location" : "Tiong Bahru","price" : 159,"hotelclass" : 2,"guestreview" : 7.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        36: {"name" : "Park View Hotel","location" : "Bugis","price" : 88,"hotelclass" : 3,"guestreview" : 7.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        37: {"name" : "Heritage Collection on Seah","location" : "Bugis","price" : 180,"hotelclass" : 3,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        38: {"name" : "InterContinental Singapore","location" : "Bugis","price" : 360,"hotelclass" : 5,"guestreview" : 8.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        39: {"name" : "Hotel Calmo Bugis","location" : "Bugis","price" : 96,"hotelclass" : 3,"guestreview" : 7.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        40: {"name" : "Hotel Nuve Heritage","location" : "Bugis","price" : 164,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        41: {"name" : "Pan Pacific Serviced Suites Beach Road","location" : "Bugis","price" : 313,"hotelclass" : 5,"guestreview" : 8.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        42: {"name" : "Wanderlust, The Unlimited Collection by Oakwood","location" : "Little India","price" : 156,"hotelclass" : 4,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        43: {"name" : "The Daulat by Hotel Calmo","location" : "Little India","price" : 92,"hotelclass" : 3,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        44: {"name" : "The Great Madras","location" : "Little India","price" : 66,"hotelclass" : 4,"guestreview" : 7.4,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        45: {"name" : "ST Signature Jalan Besar","location" : "Little India","price" : 88,"hotelclass" : 3,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        46: {"name" : "Hotel 81 Dickson","location" : "Little India","price" : 63,"hotelclass" : 2,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        47: {"name" : "Hotel 81 Rochor","location" : "Little India","price" : 57,"hotelclass" : 2,"guestreview" : 7.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        }

mainprogram()
=======
        list=['Marina Bay','Orchard Road','Chinatown','Sentosa','Clarke Quay']
        droplist=OptionMenu(main_frame, self.location_var, *list)
        droplist.config(width=20, font=('times new roman',14), bg='white')
        droplist.grid(row=1,column=1,padx=10,sticky=W)

        #Hotel Rating
        hotel_rating=Label(main_frame,text='Hotel Rating:',font=('times new roman',14,'bold'))
        hotel_rating.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        rating_frame=Frame(main_frame)
        rating_frame.grid(row=2,column=1,columnspan=5,pady=25,sticky=W)

        radio_1 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=1, text='1', font=('times new roman', 14))
        radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
        radio_2 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=2, text='2', font=('times new roman', 14))
        radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
        radio_3 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=3, text='3', font=('times new roman', 14))
        radio_3.grid(row=0, column=2, padx=10, pady=0, sticky=W)
        radio_4 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=4, text='4', font=('times new roman', 14))
        radio_4.grid(row=0, column=3, padx=10, pady=0, sticky=W)
        radio_5 = Radiobutton(rating_frame, variable=self.hotel_rating_var, value=5, text='5', font=('times new roman', 14))
        radio_5.grid(row=0, column=4, padx=10, pady=0, sticky=W)
        
        
        #Price
        price=Label(main_frame,text='Price Budget:',font=('times new roman',14,'bold'))
        price.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        scale_frame=Frame(main_frame)
        scale_frame.grid(row=3, column=1, padx=10, pady=0, sticky=W)
        scale_min = Scale(scale_frame, from_=100, to=900, orient=HORIZONTAL, length=350, variable=self.price)
        scale_min.set(200)
        scale_min.pack(side=LEFT,ipady=8)
        

        #Breakfast
        optional_msg=Label(secondary_frame,text='Optional',font=('times new roman',10,'bold','underline'),fg='darkblue')
        optional_msg.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        breakfast=Label(secondary_frame,text='Breakfast Availability:',font=('times new roman',14,'bold'))
        breakfast.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        breakfast_frame=Frame(secondary_frame)
        breakfast_frame.grid(row=1,column=1,columnspan=5,pady=0,sticky=W)

        breakfast_radio_1 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='1', text='Yes', font=('times new roman', 14))
        breakfast_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
        breakfast_radio_2 = Radiobutton(breakfast_frame, variable=self.breakfast_var, value='0', text='No', font=('times new roman', 14))
        breakfast_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
        

        #Shuttlebus Service
        shuttle_service=Label(secondary_frame,text='Shuttle Service Availability:',font=('times new roman',14,'bold'))
        shuttle_service.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        shuttle_service_frame=Frame(secondary_frame)
        shuttle_service_frame.grid(row=2,column=1,columnspan=5,pady=0,sticky=W)

        shuttle_radio_1=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='1',text='Yes',font=('times new roman',14))
        shuttle_radio_1.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        shuttle_radio_2=Radiobutton(shuttle_service_frame, variable=self.shuttlebus_var, value='0',text='No',font=('times new roman',14))
        shuttle_radio_2.grid(row=0,column=1,padx=10,pady=0,sticky=W)

        #Spa
        spa=Label(secondary_frame,text='Spa Availability:',font=('times new roman',14,'bold'))
        spa.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        spa_frame=Frame(secondary_frame)
        spa_frame.grid(row=3,column=1,columnspan=5,pady=0,sticky=W)
        spa_radio_1 = Radiobutton(spa_frame, variable=self.spa_var, value='1', text='Yes', font=('times new roman', 14))
        spa_radio_1.grid(row=0, column=0, padx=10, pady=0, sticky=W)
        spa_radio_2 = Radiobutton(spa_frame, variable=self.spa_var, value='0', text='No', font=('times new roman', 14))
        spa_radio_2.grid(row=0, column=1, padx=10, pady=0, sticky=W)
    
        
        #Button Frame
        button_frame=Frame(secondary_frame,bd=2,relief=RIDGE)
        button_frame.place(x=34,y=250,width=480,height=70)

        
        search_button=Button(button_frame,text='Search',command=self.validation,font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='green',fg='white')
        search_button.grid(row=0,column=0,padx=23,pady=13,sticky=W)

        clear_button=Button(button_frame,text='Clear Data',font=("times new roman",15,'bold'),width=12,cursor='hand2',bg='red',fg='white', command=self.clearData)
        clear_button.grid(row=0,column=2,padx=100,pady=13,sticky=W)

              

root=Tk()
obj=Register(root)
root.mainloop()
>>>>>>> 9b473125ddfc9f00d29b58ca76f219f89f055c66:input.py
