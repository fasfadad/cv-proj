from tkinter import ttk
from random import randint, choice
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk



def main_screen(root): 
    hotelmain = {
        1: {"name" : "Pan Pacific Singapore", "photo" : "panpacific.png", "location" : "Marina Bay","price" : 282,"hotelclass" : 5,"guestreview" : 8.8,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        2: {"name" : "Parkroyal Collection Marina Bay","location" : "Marina Bay","price" : 320,"hotelclass" : 5,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
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
    
    global screen

    screen = root
    screen.geometry("900x800")
    screen.configure(bg="#d7dae2")
    screen.title("Hotel List")

    counter=28
    for x, hotel in hotelmain.items():
        hotelnamex = hotel["name"]
        price = hotel["price"]
        rating = hotel["hotelclass"]
        breakfast = hotel["freebreakfast"]
        if(breakfast):
            breakfast = 'Yes'
        else:
            breakfast = 'No'
        bus = hotel["shuttlebusservice"]
        if(bus):
            bus = 'Yes'
        else:
            bus = 'No'
        spa = hotel["spa"]
        if(spa):
            spa = 'Yes'
        else:
            spa = 'No'
    
        hotel1=Image.open('panpacific.png')
        hotel1=hotel1.resize((400,260),Image.ANTIALIAS)
        photo_logo1=ImageTk.PhotoImage(hotel1)

        hotel1_frame=Frame(root,bd=5,relief=RIDGE)
        hotel1_frame.place(x=30,y=counter,width=820,height=4000)

        placement1=Label(hotel1_frame,image=photo_logo1,compound=LEFT)
        placement1.place(x=10,y=15)


        hotelname=Label(hotel1_frame,text=hotelnamex, font=('times new roman',18,'bold'),fg='darkblue')
        hotelname.grid(row=0,column=0,padx=430,pady=20,sticky=W)
        info=Label(hotel1_frame,text='Price: $' + str(price), font=('times new roman',12,'bold'))
        info.grid(row=1,column=0,padx=430,pady=5,sticky=W)
        info=Label(hotel1_frame,text='Hotel Rating: ' + str(rating), font=('times new roman',12,'bold'))
        info.grid(row=2,column=0,padx=430,pady=5,sticky=W)
        info=Label(hotel1_frame,text='Breakfast Availability: ' + breakfast, font=('times new roman',12,'bold'))
        info.grid(row=3,column=0,padx=430,pady=5,sticky=W)
        info=Label(hotel1_frame,text='Shuttle Service Availability: ' + bus, font=('times new roman',12,'bold'))
        info.grid(row=4,column=0,padx=430,pady=5,sticky=W)
        info=Label(hotel1_frame,text='Spa Availability: ' + spa, font=('times new roman',12,'bold'))
        info.grid(row=5,column=0,padx=430,pady=5,sticky=W)

        counter+=300


    scrollbar=ttk.Scrollbar(screen,orient='vertical')
    scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')
 
    screen.bind('<MouseWheel>', lambda event: screen.yview_scroll(20,"units"))
    
    screen.mainloop()

root = Tk()
main_screen(root)

