from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
root.minsize(height=800,width=1500)
def tab1():
    def tab2():
        page1.destroy()
        button1.destroy()
        class Register():

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


        def back():
            page2.destroy()
            button2.destroy()
            tab1()

        button2=Button(root,text='Back',font=('times new roman',25), command=back)
        button2.pack(side=BOTTOM)

    page1=Label(root,text='Main Page', font=('times new roman',30))
    page1.pack()
    button1=Button(root,text='Next',font=('times new roman',25), command=tab2)
    button1.pack(side=BOTTOM)

tab1()
root.mainloop()
