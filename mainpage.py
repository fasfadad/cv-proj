from tkinter import*

root=Tk()
root.minsize(height=500,width=900)
def tab1():
    def tab2():
        page1.destroy()
        button1.destroy()
        page2=Label(root,text='Second Page', font=('times new roman',30))
        page2.pack()
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
